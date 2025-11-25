import json
from backend.agent.registry import current_state
from backend.workflow.loop_workflow import LoopWorkflow
from backend.utils.file_validator import FileValidator

# ---- Mock bad JSON ----
BROKEN_JSON = """
{
  "path":"src/app/login.page.ts"
  "content": "export class LoginPageComponent {}"
}
"""  # ❌ missing comma after path


def simulate_generation_override():
    """
    Instead of LLM, we simulate broken raw JSON from code generation.
    """
    current_state.spec_clean = "A login screen where users enter their account credentials."
    current_state.feature_plan = {
        "app_name": "Test App",
        "features": [
            {
                "canonical_name": "Login",
                "selector": "app-login",
                "route": "/login",
                "file_name": "login.page.ts",
                "class_name": "LoginPageComponent",
                "description": "Users enter credentials."
            }
        ]
    }
    return BROKEN_JSON


def test_fix_agent_integration():
    print("\n================ FIX INTEGRATION TEST ================")

    # Prepare test workflow
    workflow = LoopWorkflow()

    # Manually inject broken JSON into handler
    # Force _handle_file to process BROKEN_JSON
    file_path = "login.page.ts"
    raw = simulate_generation_override()

    print("\nRAW BROKEN JSON RECEIVED:")
    print(raw)

    # Check that broken JSON is indeed invalid
    print("\nValidator says JSON is valid? ->", FileValidator.is_valid(raw))

    # Call the system to handle the file entirely (generation overridden)
    workflow._handle_file(file_path)

    print("\nState Files JSON Output:")
    print(json.dumps(current_state.files_json, indent=2))

    print("\nRecorded Errors:")
    print(json.dumps([e for e in current_state.errors], indent=2))

    print("\nSymbols Extracted:")
    print(json.dumps(current_state.symbols, indent=2))

    print("\n=======================================================\n")


if __name__ == "__main__":
    test_fix_agent_integration()
