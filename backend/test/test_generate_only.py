
from backend.agent.registry import current_state
from backend.agent.generation_agent import GenerationAgent
from backend.utils.file_validator import FileValidator

# GIVEN:
current_state.raw_user_prompt = "create a login page"
current_state.spec_clean = "Create a login page with email & password + submit."

# Target test file:
test_file = "src/app/login.page.ts"

agent = GenerationAgent()

print("\n🔄 Generating file...")
raw = agent.generate(test_file)

print("\n📌 Raw JSON from generator:")
print(raw)

print("\n🧪 Validating JSON...")
valid = FileValidator.is_valid(raw)
print("Validation Result:", "✔️ OK" if valid else "❌ INVALID")
