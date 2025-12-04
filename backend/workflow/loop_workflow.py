from backend.agent.generation_agent import GenerationAgent
from backend.utils.file_validator import FileValidator
from backend.agent.registry import current_state
from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.utils.system_context_builder import SystemContextBuilder
from backend.agent.feature_planning_agent import FeaturePlanningAgent
from backend.utils.json_fix_prompt_builder import JSONFixPromptBuilder
from backend.agent.fix_agent import FixAgent
from backend.utils.symbol_extractor import SymbolExtractor
from backend.utils.file_writer import FileWriter
from backend.vectorstore.code_indexer import CodeIndexer


from backend.utils.folder_zipper import zip_folder
from backend.settings import BASE_DIR, GENERATED_DIR
from pathlib import Path
from uuid import uuid4

class LoopWorkflow:
    def __init__(self):
        self.agent = GenerationAgent()
        self.indexer = CodeIndexer()

    def run(self):
        
        # 0) Clear previous index
        print("Clearing previous vector index...")
        self.indexer.reset_index()

        # 1) Prompt engineering
        PromptEngineeringAgent().run()
        print(f"successufly Engineered the Prompt.....")
        print("="*50)

        # 2) Feature planning 
        plan = FeaturePlanningAgent().run()
        print(f"successufly Planned The project features.....")
        print("="*50)
        print(plan)

        # 3) Collect planned file targets
        file_queue = self._collect_files()  
        print("\n Files to generate:\n", file_queue)
        print("="*50)

        # 4) Generate each file based on planning
        for file_path in file_queue:
            self._handle_file(file_path)
            
            
            
            
            
        # 5) Output summary and write files
        print("\n All files generated successfully!")
        print("\n Final valid JSON files:")

        for path in current_state.files_json.keys():
            print("(-_-)", path)
        print("="*50)

        print("==> writing files.....")
        writer = FileWriter("generated_output")  # your output directory
        writer.write_files(current_state.files_json)

        print("==> Indexing files.....")
        self._index_files_into_vectordb()
        print("successfully indexed files.")

        
        print("="*50)
        print("zipping folder.....")
        zip_folder(GENERATED_DIR, BASE_DIR) #zip and delete source
        print("your zip is ready.")

        

    def _collect_files(self):
        plan = current_state.feature_plan

        # The new feature plan already contains an ordered list of all files.
        planned_files = plan.get("files", [])

        file_queue = []

        for entry in planned_files:
            path = entry.get("path")
            if path:
                file_queue.append(path)

        return file_queue



    def _handle_file(self, file_path: str):
        print(f"\n ==> Generating: {file_path}")

        # Up to 3 attempts: generate → repair → regenerate
        for attempt in range(3):
            raw = self.agent.generate(file_path)

            # 1) First try direct validation
            if FileValidator.is_valid(raw):
                parsed = self._parse_and_store(file_path, raw)
                self._extract_and_store_symbols(file_path, parsed["content"])
                self._rebuild_system_context()
                print(f"SUCCESS: {file_path}")
                print("="*50)
                return

            print(f"(X) INVALID JSON for {file_path} on attempt {attempt+1}. Trying repair...")

            # 2) Try FixAgent
            fixer = FixAgent()
            repaired = fixer.run(file_path, raw, JSONFixPromptBuilder)

            # 3) Validate the repaired result
            if repaired and FileValidator.is_valid(repaired):
                parsed = self._parse_and_store(file_path, repaired)
                self._extract_and_store_symbols(file_path, parsed["content"])
                self._rebuild_system_context()
                print(f"FIXED + SUCCESS: {file_path}")
                print("="*50)
                return

            print("(X) Repair failed. Will retry full generation...")

        # If we reach here → three failures
        print(f"(X) FAILED PERMANENTLY: {file_path}")
        current_state.errors.append({
            "file": file_path,
            "type": "GENERATION_FAILURE",
            "message": "Unable to generate or repair JSON after 3 attempts",
            "severity": "critical"
        })

        
    def _parse_and_store(self, file_path: str, raw: str):
        parsed = FileValidator.parse_llm_json(raw)
        current_state.files_json[file_path] = parsed
        return parsed

    def _extract_and_store_symbols(self, file_path: str, code: str):
        extracted = SymbolExtractor.extract_symbols(code)
        for sym in extracted:
            sym["path"] = file_path
            current_state.symbols.append(sym)
        
    def _rebuild_system_context(self):
        current_state.system_context = SystemContextBuilder().build()

    # index files in the vector store
    def _index_files_into_vectordb(self):
        self.indexer.index_project("generated_output/src/app")

        

    # def _handle_file(self, file_path: str):
    #     print(f"\n ==> Generating: {file_path}")

    #     raw = self.agent.generate(file_path)   # generate the file.
        
        
    #     if FileValidator.is_valid(raw):
    #         parsed = FileValidator.parse_llm_json(raw)
    #         current_state.files_json[file_path] = parsed

            
    #         # extract and store symbols
    #         code = parsed["content"]
    #         extracted = SymbolExtractor.extract_symbols(code)
    #         for sym in extracted:
    #             sym["path"] = file_path  # attach file path
    #             current_state.symbols.append(sym)
    #             print(current_state.symbols)

    #         # build the system context again to add the files path that has been generated.
    #         current_state.system_context = SystemContextBuilder().build()

    #         print(f"SUCCESS: {file_path}")
    #     else:
    #         print(f"(X) INVALID: {file_path}")
    #         current_state.errors.append({
    #             "file": file_path,
    #             "type": "VALIDATION",
    #             "message": "JSON failed schema validation",
    #             "severity": "error"
    #         })



