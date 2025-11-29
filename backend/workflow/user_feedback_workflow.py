from backend.utils.file_validator import FileValidator
from backend.utils.symbol_extractor import SymbolExtractor
from backend.vectorstore.code_indexer import CodeIndexer
from backend.agent.registry import current_state
from backend.agent.patch_apply_agent import PatchApplyAgent
from backend.agent.patch_planning_agent import PatchPlanningAgent
from backend.utils.code_search import CodeSearch
from backend.utils.file_writer import FileWriter
from backend.settings import BASE_DIR, GENERATED_DIR
from backend.utils.folder_zipper import zip_folder
import os

def _normalize_updated_files_for_writer(updated_files: dict, output_dir: str) -> dict:
    """
    Return dict where keys are RELATIVE paths under output_dir (e.g. "src/app/xxx.ts")
    and values are dict with 'content' string.
    """
    normalized = {}
    out_dir = os.path.abspath(output_dir)

    for path, data in updated_files.items():
        # if data is a dict, get content; else assume string content
        if isinstance(data, dict) and "content" in data:
            content = data["content"]
        elif isinstance(data, str):
            content = data
        else:
            raise ValueError(f"Unsupported updated_files value for {path}: {type(data)}")

        abs_path = os.path.abspath(path)

        # If path is already inside output_dir, make relpath
        if abs_path.startswith(out_dir):
            rel = os.path.relpath(abs_path, out_dir)  # e.g. "src/app/login-screen.page.ts"
        else:
            # path might be relative already; try to use it as-is
            # ensure it uses forward slashes for your app
            rel = path.replace(os.path.sep, "/")

        # Keep consistent: ensure it starts with "src/app/"
        if not rel.startswith("src/app/"):
            rel = os.path.join("src", "app", rel).replace(os.path.sep, "/")
        
        while rel.startswith("src/app/src/app/"):
            rel = rel.replace("src/app/src/app/", "src/app/", 1)

        normalized[rel] = {"content": content}

    return normalized




class UserFeedbackWorkflow:
    def __init__(self):
        self.indexer = CodeIndexer()
        
    def run(self):
     

        # check if the prompt is empty
        if not current_state.modify_prompt:
            raise ValueError("modify_prompt is empty")

        print("\n=== Step 1: Searching for Relevant Code ===")
        search = CodeSearch.run(current_state.modify_prompt)
        print(search)

        print("\n===  Step 2: Generating Patch Plan ===")
        PatchPlanningAgent().run(
            user_prompt=current_state.modify_prompt,
            code_snippets=current_state.search_results
        )
        
        if not current_state.patch_plan.get("changes"):
            return "No matching code found for this request"
        
        print("\n===  Step 3: Applying Patches ===")
        PatchApplyAgent().run()
        

        print("\n=== Step 4: Writing Updated Files ===")
        writer = FileWriter("generated_output")
        normalized_files = _normalize_updated_files_for_writer(current_state.updated_files, writer.output_dir)
        writer.write_files(normalized_files)

        
        



        print("\n===  Step 5: Re-indexing Updated Files ===")
        self.indexer.update_file_chunks(normalized_files)

        print("\n===  Step 6: Zipping the Folder ===")
        zip_folder(GENERATED_DIR, BASE_DIR) #zip and delete source
        print("your zip is ready.")

        def _parse_and_store(self, file_path: str, raw: str):
            parsed = FileValidator.parse_llm_json(raw)
            current_state.files_json[file_path] = parsed
            return parsed

        def _extract_and_store_symbols(self, file_path: str, code: str):
            extracted = SymbolExtractor.extract_symbols(code)
            for sym in extracted:
                sym["path"] = file_path
                current_state.symbols.append(sym)



