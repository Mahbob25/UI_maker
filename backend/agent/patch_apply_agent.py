""""what i qnt is a agnet that takes the plan the file and preduce the new code""" 
# input
# full file content.
# instructions => current_state.patch.plan
# excerp => current_state.patch.plan
# reason => current_state.patch.plan


# expected output:
# {"updated_content": "full code"}
from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient
from google.genai import types
import json
import json_repair
class PatchApplyAgent:
    def __init__(self):
        self.client = LLMClient.get()

    def run(self):
        changes = current_state.patch_plan["changes"]

        # Build user content (NOT the system prompt)
        user_content = {
            "changes": []
        }

        for change in changes:
            file_path = change["file"]

            # Load full file content safely
            with open(file_path, "r", encoding="utf-8") as f:
                full_code = f.read()

            user_content["changes"].append({
                "file": file_path,
                "reason": change["reason"],
                "instructions": change["instructions"],
                "excerpt": change["current_code_excerpt"],
                "full_file": full_code,
            })

        # Convert dict to JSON
        json_blob  = json.dumps(user_content, indent=2, ensure_ascii=False)
        user_message = f"""
Here is a list of code changes that must be applied.

Each item contains:
- file (full path)
- full_file (the entire file before modification)
- excerpt (a hint for where the change is)
- instructions (the exact change needed)

You MUST apply modifications exactly as described.

INPUT JSON:
```json
{json_blob}
"""

        system_context = """
You are a PATCH APPLY AGENT.

Your ONLY job:
Given the full file content + the change instructions, you must return the FULL UPDATED FILE.

RULES:
- Do NOT invent additional edits.
- Do NOT reformat the file.
- Do NOT remove or reorder imports unless needed by the requested change.
- Apply ONLY the requested modification.
- Preserve indentation, whitespace, and formatting exactly as-is.
- Keep code style identical to the original.
- If the snippet appears multiple times, modify ONLY the occurrence that most closely matches the surrounding context.
- Do NOT add explanations, comments, or markdown.

- Return ONLY strict JSON:
{
  "updated_files": [
    {
      "file": "full file path",
      "updated_content": "<FULL FILE WITH WELCOME BACK USER>"
    },
    {
      "file": "full file path",
      "updated_content": "<FULL FILE WITH FEEL THE DIFFERENCE>"
    }
  ]
}

INPUTS PROVIDED TO YOU:
- full_file: the entire file content BEFORE the change
- excerpt: a small code segment where the change should happen
- instructions: the required modification described in natural language
- reason: why this change is needed (helps you choose correct region)

END OF RULES.

""" 

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_context,
                response_mime_type="application/json"
            ),
            contents=user_message
        )

        
        
        try:
            result = json.loads(response.text)
        except Exception:
            result = json_repair.loads(response.text)
            try:
                result = json.loads(response.text)
            except Exception:
                raise ValueError("PatchApplyAgent returned invalid JSON")
            
        
        # Normalize to dict form
        updated_list = result.get("updated_files", [])

        if not isinstance(updated_list, list):
            raise ValueError("PatchApplyAgent output: 'updated_files' must be a list.")

        normalized = {}

        for item in updated_list:
            if "file" not in item or "updated_content" not in item:
                raise ValueError("PatchApplyAgent returned an invalid item: missing 'file' or 'updated_content'.")

            file_path = item["file"]
            content = item["updated_content"]

            normalized[file_path] = {
                "content": content
            }

        # Save to state
        current_state.updated_files = normalized
        
        return normalized

        