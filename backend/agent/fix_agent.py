import json
from backend.utils.llm_client import LLMClient
from backend.agent.registry import current_state
from google.genai import types
from backend.utils.file_validator import FileValidator



class FixAgent:
    """
    General purpose Fix Agent. Repair malformed outputs using the appropriate
    prompt builder (e.g., JSONFixPromptBuilder).
    """

    def __init__(self):
        self.client = LLMClient.get()

    def run(self, file_path: str, raw_text: str, prompt_builder) -> str:
        if not prompt_builder:
            raise ValueError("FixAgent requires a prompt builder object.")

        prompt = prompt_builder.build(file_path, raw_text)

        response = self.client.models.generate_content(
            model=current_state.user_selected_model,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
            contents=prompt,
        )

        fixed = response.text or ""

        # Validate ONLY JSON structure — DO NOT SAVE ANYTHING
        try:
            if FileValidator.is_valid(fixed):
                return fixed  # Pass to handler normally
        except Exception:
            pass

        # if still invalid — mark error and return original
        current_state.errors.append({
            "file": file_path,
            "type": "JSON_FIX_FAILED",
            "message": "FixAgent could not repair JSON",
            "severity": "error"
        })

        return raw_text  # return original for logging/debug
