from backend.agent.generation_agent import GenerationAgent
from backend.agent.file_validator import FileValidator
from backend.agent.registry import current_state
from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.agent.system_context_builder import SystemContextBuilder
from backend.agent.feature_extraction_agent import FeatureExtractionAgent

class LoopWorkflow:
    def __init__(self):
        self.agent = GenerationAgent()

    def run(self):
        
        # Generating Workflow
        PromptEngineeringAgent().run()
        print(f"successufly Engineered the Prompt.....")
        print("\n" + "="*50)

        SystemContextBuilder().build()
        print(f"successufly built the context and output Rules.....")
        print("\n" + "="*50)

        FeatureExtractionAgent().run()
        print(f"successufly Extracted features form user spec.....")
        print("\n" + "="*50)
        print(current_state.project_metadata.feature_files)

        file_queue = self._collect_files()   #===> this is a helper function, defiend below.
        print("\n Files to generate:", file_queue)

        for file_path in file_queue:
            self._handle_file(file_path)     #===> this is a helper loop function, defiend below.

        print("\n All files generated successfully!")
        print("\n Final valid JSON files:")
        for path in current_state.files_json.keys():
            print("(-_-)", path)

    def _collect_files(self):
        files = set(
            current_state.project_metadata.base_files +
            current_state.project_metadata.feature_files
        )
        return list(files)

    def _handle_file(self, file_path: str):
        print(f"\n ==> Generating: {file_path}")

        raw = self.agent.generate(file_path)   # generate the file.

        if FileValidator.is_valid(raw):
            current_state.files_json[file_path] = FileValidator.parse_llm_json(raw)
            # we need to extract relievant iformation to pass it
            generated_files_so_far = current_state.files_json.items()
            
            print(f"SUCCESS: {file_path}")
        else:
            print(f"(X) INVALID: {file_path}")
            current_state.errors.append({
                "file": file_path,
                "type": "VALIDATION",
                "message": "JSON failed schema validation",
                "severity": "error"
            })



