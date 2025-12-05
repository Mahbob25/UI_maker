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
import os
class PatchApplyAgent:
    def __init__(self):
        self.client = LLMClient.get()

    def run(self):

        changes = current_state.patch_plan["changes"]

        # build the metadata
        metadata_changes = []
        for change in changes:
            metadata_changes.append({
                "file": change["file"],
                "reason": change["reason"],
                "instructions": change["instructions"],
                "excerpt": change["current_code_excerpt"],
            })

        json_meta = json.dumps(
            {"changes": metadata_changes},
            indent=2,
            ensure_ascii=False
        )

        
        # 2. Build <file> blocks with full file content
        
        file_blocks = ""
        for change in changes:
            file_path = change["file"]

            # SAFE PATH FIX
            if os.path.basename(file_path) == file_path:
                file_path = os.path.join("generated_output", "src", "app", file_path)

            if not os.path.exists(file_path):
                raise FileNotFoundError(
                    f"File not found: {file_path} (resolved from '{change['file']}')"
                )

            with open(file_path, "r", encoding="utf-8") as f:
                full_code = f.read()


            file_blocks += f"""
    <file path="{file_path}">
    {full_code}
    </file>
    """
        print("full code ====>", full_code)
 
    # 3. Build the full prompt
 
        user_prompt = f"""
    You are a code-editing agent.  
    Your task is to update files based on the user's requested changes.

    RULES:
    1. Use the FULL FILE CONTENTS provided below only as READ-ONLY context.
    2. NEVER include full file content in your output except in "updated_code".
    3. Only output a valid JSON object. No explanations, no markdown.
    4. Apply ONLY the changes described in CHANGES METADATA.
    5. Do NOT modify anything else in the file.
    6. If multiple edits target the same file, produce one merged update.

    --------------------------------------------
    CHANGES METADATA (small JSON)
    --------------------------------------------
    ```json
    {json_meta}
FULL FILE CONTENTS (context only — DO NOT RETURN THESE)

{file_blocks}
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
If the provided code excerpt does NOT appear in the file:
- Do NOT abort.
- Do NOT skip the file.
- Instead, follow the INSTRUCTIONS and perform the best possible modification.
- If the target code does not exist, ADD it in the most reasonable location.

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
You MUST apply ALL patches listed in "changes". 

For each item in the "changes" array:
- Locate the exact current_code_excerpt inside the file.
- Apply ONLY the specified change.
- Do NOT skip any item.
- Do NOT merge or combine patches.
- Process them sequentially, from first to last.
- Output the full updated file content after ALL patches are applied.

DO NOT stop after the first match.
DO NOT assume the user wants only one change.
You MUST apply every patch in the "changes" list.


##DOM EDITING RULES (VERY IMPORTANT):
For EVERY user-visible text element:
- Add contenteditable="true"
- Add a unique stable DOM identifier using the attribute: data-id="..."
- IDs MUST follow this naming convention:
    <section_name>_<element_type>_<index>
  Example: hero_title, hero_subtitle, services_card_1_title, footer_text

Rules:
1. Every heading (h1, h2, h3, h4), paragraph (p), span, button text, and link text MUST have:
       contenteditable="true"
       data-id="..."
2. Icons, images, wrappers, and layout divs MUST NOT be editable.
3. Use stable IDs derived from the feature name from the planning agent.
4. NEVER generate random IDs (no UUIDs, no hashes).
5. The index must be sequential per section (e.g., service_card_1, service_card_2).
6. The user must be able to edit all text directly via the browser.

Example:
<h1 data-id="hero_title" contenteditable="true">Next Generation IT Agency</h1>

<p data-id="services_card_1_desc" contenteditable="true">
   We build modern web applications.
</p>

<button data-id="cta_button" contenteditable="true">
   Get Started
</button>

These rules MUST be applied to ALL generated HTML output.

END OF RULES.

""" 

        response = self.client.models.generate_content(
            model=current_state.user_selected_model,
            config=types.GenerateContentConfig(
                system_instruction=system_context,
                response_mime_type="application/json"
            ),
            contents=user_prompt
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

        