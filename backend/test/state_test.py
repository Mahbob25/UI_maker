from pydantic import ValidationError
from backend.agent.state import AgentState, ErrorDetail


def test_state_schema():
    print("\n" + "="*50)
    print(" TESTING State Schema Verification...")
    print("="*50)

    # 1. Create initial State instance [cite: 6]
    state = AgentState()
    print(f"State initialized. Raw prompt is empty: '{state.raw_user_prompt}'")

    # 2. Simulate Step 1: specific user prompt [cite: 13]
    state.raw_user_prompt = "Create a login page with Angular Material"
    print(f"User prompt stored: '{state.raw_user_prompt}'")

    # 3. Simulate Step 2: storing a cleaned spec [cite: 24]
    state.spec_clean = "Feature: Login. Requirements: Reactive Forms, MatInput."
    print(f"Spec stored.")

    # 4. Simulate Step 5 (Validation): Adding structured errors [cite: 39]
    # We specifically test the ErrorDetail structure here
    new_error = ErrorDetail(
        file="src/app/app.component.ts",
        type="TS",
        message="Missing import for Component",
        severity="error"
    )
    state.errors.append(new_error)
    
    # 5. Verify persistence [cite: 8]
    print("\n--- FINAL STATE DUMP ---")
    print(state.model_dump_json(indent=2))

    assert state.raw_user_prompt == "Create a login page with Angular Material"
    assert len(state.errors) == 1
    assert state.errors[0].file == "src/app/app.component.ts"
    
    print("\nTEST PASSED: State Schema is valid and persists data correctly.")
    print("="*50 + "\n")
if __name__ == "__main__":
    test_state_schema()