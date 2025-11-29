# test_patch_agent.py
import json
import os
from backend.agent.patch_apply_agent import PatchApplyAgent
from backend.agent.registry import current_state

# ─────────────────────────────────────────────────────────────
# 1. Create a fake project structure (temp files for testing)
# ─────────────────────────────────────────────────────────────
os.makedirs("generated_output/src/app", exist_ok=True)

# File 1: login-screen.page.ts
with open("generated_output/src/app/login-screen.page.ts", "w", encoding="utf-8") as f:
    f.write("""import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  template: `
    <div class="login-container">
      <h2>Welcome Back!</h2>
      <p>Please sign in to continue</p>
      <button>Login</button>
    </div>
  `
})
export class LoginScreenPageComponent {}
""")

# File 2: register-screen.page.ts
with open("generated_output/src/app/register-screen.page.ts", "w", encoding="utf-8") as f:
    f.write("""import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  template: `
    <div class="register-container">
      <h2>create an account</h2>
      <form>
        <input placeholder="Email" />
        <button>Sign Up</button>
      </form>
    </div>
  `
})
export class RegisterScreenPageComponent {}
""")

# ─────────────────────────────────────────────────────────────
# 2. Simulate the exact patch_plan your planner produces
# ─────────────────────────────────────────────────────────────
current_state.patch_plan = {
    "changes": [
        {
            "file": "generated_output/src/app/login-screen.page.ts",
            "reason": "User wants new header",
            "current_code_excerpt": "<h2>Welcome Back!</h2>",
            "instructions": "Change text to 'Welcome Back User!'"
        },
        {
            "file": "generated_output/src/app/register-screen.page.ts",
            "reason": "User wants new header",
            "current_code_excerpt": "<h2>create an account</h2>",
            "instructions": "Change text to 'Feel the difference!'"
        }
    ]
}

# ─────────────────────────────────────────────────────────────
# 3. Run the PatchApplyAgent
# ─────────────────────────────────────────────────────────────
print("Running PatchApplyAgent...\n")
agent = PatchApplyAgent()
result = agent.run()

# ─────────────────────────────────────────────────────────────
# 4. Pretty print the result
# ─────────────────────────────────────────────────────────────
print("AGENT RESPONSE:")
print(json.dumps(result, indent=2))

# ─────────────────────────────────────────────────────────────
# 5. Verify it worked (optional auto-check)
# ─────────────────────────────────────────────────────────────
updated_files = result.get("updated_files", [])
success = True

for updated in updated_files:
    file_path = updated["file"]
    content = updated["updated_content"]
    
    if "Welcome Back User!" in content:
        print(f"SUCCESS: {file_path} → header updated correctly")
    elif "Feel the difference!" in content:
        print(f"SUCCESS: {file_path} → header updated correctly")
    else:
        print(f"FAILED: {file_path} → change not applied!")
        success = False

if success:
    print("\nALL TESTS PASSED! Your PatchApplyAgent works perfectly!")
else:
    print("\nOne or more changes failed.")