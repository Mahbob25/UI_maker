from backend.agent.registry import current_state
from backend.agent.feature_extraction_agent import FeatureExtractionAgent

if __name__ == "__main__":
    # assume spec_clean already set, or set it manually here:
    current_state.spec_clean = """
    The system should have a login screen, a main dashboard, and a profile editor
    where users can update their personal information.
    """ 
    

    files = FeatureExtractionAgent().run()
    print("Extracted feature files:", files)
    print("Extracted feature files:", current_state.project_metadata.base_files)

