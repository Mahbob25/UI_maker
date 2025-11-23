from backend.agent.prompt_engineering_agent import PromptEngineeringAgent
from backend.agent.registry import current_state
def test_prompt_engineering():
    print("\n" + "="*50)
    print(" TESTING PromptEngineeringAgent")
    print("="*50)
    test_input = input("Enter test input:\n")
    try: 
        result = PromptEngineeringAgent().run(test_input)
        if result:
            print("SUCCESS: Agent returned a valid prompt")
            print(f"Prompt length: {len(current_state.spec_clean)} chars") #conforms is was saved in the state.
        else:
            print("FAILED: No agent did not return a valid prompt")
    except Exception as e:
        print(f"An unexpected error occurred in PromptEngineeringAgent: {e}")
    finally:
        print("="*50 + "\n")


if __name__ == "__main__":
    test_prompt_engineering()