
class JSONFixPromptBuilder:
    """
    Generates a strict repair prompt to fix malformed JSON responses
    from the LLM without changing semantics of the output.
    """

    @staticmethod
    def build(file_path: str, raw_text: str) -> str:
        return f"""
You are a JSON Repair Agent.

Your task:
Fix the malformed JSON output below WITHOUT altering any values
or changing the file path or file content.

# RULES
- Only fix JSON syntax issues (quotes, commas, brackets).
- Do NOT change keys. Do NOT change values.
- Do NOT remove existing data.
- The JSON MUST have EXACT shape:

{{
  "path": "{file_path}",
  "content": "<unchanged full file content>"
}}

# REQUIRED BEHAVIOR
- The "path" MUST be exactly: "{file_path}"
- NEVER modify any characters in the "content" string except for escaping rules if needed.
- Do NOT add explanations, comments, or extra text.
- Output ONLY valid JSON.

# BROKEN JSON INPUT
RAW_JSON:
{raw_text}
"""