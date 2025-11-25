from backend.agent.registry import current_state
from backend.agent.feature_planning_agent import FeaturePlanningAgent

if __name__ == "__main__":
    # assume spec_clean already set, or set it manually here:
    current_state.spec_clean = """
    The system should have a login screen, a main dashboard, and a profile editor
    where users can update their personal information.
    """ 
    

    files = FeaturePlanningAgent().run()
    print("Extracted feature files:", current_state.feature_plan)

