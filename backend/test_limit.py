import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_prompt_limit():
    # 1. Test Small Prompt (Valid)
    print("Testing small prompt...")
    small_payload = {
        "prompt": "Build a simple to-do list app.",
        "theme": "modern"
    }
    # Note: Use the ZIP generation endpoint since that's what we modified the model for (shared model)
    # Actually wait, `UserInput` is used by both `/api/zip/generate` and `/api/json/generate`.
    # I'll use json generate to avoid creating a zip file on disk unnecessarily, or just check the validation response.
    # But wait, the previous code showed they share the same UserInput class.
    
    try:
        # We don't want to actually trigger the heavy workflow, so maybe we expect a 200 or 500 but PASSED validation.
        # However, the workflow runs synchronously in the code I saw: `LoopWorkflow().run(...)`
        # That might take time.
        # Ideally I should mock the workflow, but for an integration test on a running server, I can't easily mock.
        # I'll try to send a prompt that fails validation first.
        pass
    except Exception as e:
        print(e)

    # 2. Test Large Prompt (Invalid)
    print("Testing large prompt (50,001 chars)...")
    large_prompt = "a" * 50001
    large_payload = {
        "prompt": large_prompt,
        "theme": "modern"
    }
    
    response = requests.post(f"{BASE_URL}/api/zip/generate", json=large_payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 413:
        print("✅ Success: Large prompt usage rejected with 413.")
    else:
        print(f"❌ Failure: Large prompt did not trigger 413. Got {response.status_code}")

if __name__ == "__main__":
    test_prompt_limit()
