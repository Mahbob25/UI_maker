from backend.utils.system_context_builder import SystemContextBuilder
from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient
from google.genai import types
import json

class GenerationAgent:
    """
    Generates a single file based on the current project's context.
    Only produces raw JSON and stores it in state.files_json_raw.
    """
    def __init__(self):
        self.client = LLMClient.get()
        self.context_builder = SystemContextBuilder()


    def generate(self, file_path: str):
        spec = current_state.spec_clean

        if not spec or not spec.strip():
            raise ValueError(
                "CodeGenerationAgent: spec_clean is empty. "
                "Run PromptEngineeringAgent first."
            )
        
        if not file_path or not file_path.strip():
            raise ValueError("CodeGenerationAgent: target_path cannot be empty.")
        
        
        user_prompt = f"""
Generate ONLY the TypeScript code for this single file.

Target file path:
{file_path}

Rules:
- Follow the project specification and global rules given in the system context.
- The output MUST be valid JSON with the shape:
  {{
    "path": "<file path>",
    "content": "<full TypeScript source code>"
  }}
  # FILE PATH RULES
- The JSON field "path" MUST be exactly "{file_path}".
- Do NOT change file name, folder, extension, or prefix.
- Do NOT add or concatenate ANY extra path text.
- If unsure, return the exact value: "{file_path}".

- The "path" field MUST match the target file path exactly: "{file_path}".
- Generate code for ONLY this file. Do NOT generate multiple files.
- Do NOT include any explanations, comments, markdown, or backticks outside the JSON.
- For Angular components, use standalone components with INLINE templates:
  - Use the 'template' property, NOT 'templateUrl'.
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=current_state.system_context,
                response_mime_type="application/json",
            ),
            contents=user_prompt,
        )  
        raw_text = response.text or ""
        # Store raw output WITHOUT validation
        current_state.files_json_raw[file_path] = raw_text
        

        
        return raw_text  # return raw json







