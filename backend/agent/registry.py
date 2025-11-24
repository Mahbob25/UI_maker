from backend.workflow.state import AgentState

# this fixes the error of circular import i faced
# this will be the global shared state for the entire app
current_state = AgentState()