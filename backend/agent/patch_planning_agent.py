from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient
from google.genai import types
import json

class PatchPlanningAgent():
    def __init__(self):
        self.client = LLMClient().get()

    def run(self, user_prompt: str, code_snippets: str, target_page: str = None):
        prompt = f"""
USER REQUEST:
{user_prompt}

RELEVANT CODE SNIPPETS (from semantic search):
{code_snippets}

Target Page(if provided):
{target_page}

Your task:
Analyze the snippets and create a JSON patch plan following the required schema.
"""

        system_context = """
You are a Patch Planning Agent.

Your purpose:
- Given a user request (a change or modification the user wants)
- And given code snippets retrieved using semantic search
You must produce a precise and structured PATCH PLAN describing exactly what needs to change in the codebase.

What you produce:
- You DO NOT generate any executable code.
- You DO NOT rewrite entire files.
- You ONLY generate a structured plan describing:
  • Which file should be modified
  • What exact lines or code blocks are relevant
  • What needs to change (add / remove / update)
  • A short explanation why this is the correct place

Inputs you receive:
1. User request (e.g., “Change the Login header to Welcome Back User”)
2. A list of code snippets (each includes: file path, lines, and snippet content)
2- the specific page to be modified if the user provide it.

Your Tasks:
- Analyze all provided snippets
- Identify the most relevant one(s)
- Produce a JSON plan describing modifications

Output Format (STRICT JSON):
{
  "changes": [
    {
      "file": "<file path>",
      "reason": "<why this file must be changed>",
      "current_code_excerpt": "<relevant lines you found>",
      "instructions": "<describe the exact modification needed>"
    }
  ],
  "notes": "<any important clarification for the next agent>"
}

Rules:
- NEVER generate code.
- NEVER hallucinate files that were not provided in search results.
- ALWAYS base decisions strictly on the snippets shown.
- If no snippet matches the user request, output:
  { "changes": [], "notes": "No matching code found for this request." }
- Keep instructions extremely specific, but still natural language.
- Focus on identifying location and type of edit—not writing it.
If the excerpt does not match exactly due to whitespace or formatting differences,
you MUST still find the closest matching line and apply the modification.
DO NOT return an unchanged file.
If your updated file is IDENTICAL to the original, this is an error.
You MUST apply the requested change even if matching the snippet is imperfect.


When extracting the CURRENT_CODE_EXCERPT:
- Include ONLY the exact line(s) that must be edited.
- NEVER include surrounding or adjacent lines.
- Do NOT include descriptions, comments, or parent tags unless the instruction explicitly requires modifying them.
- The excerpt must be the minimal text needed for the patch agent to locate the right code.
- If the item to be changed is within an HTML tag, include ONLY that tag.
If the user specifies a target file name, OR if the target file name exists in the project metadata, 
you MUST produce a change plan even if no code snippet was provided.
If code snippet is missing: 
- Assume the file exists and plan the changes based on the user's instructions.
- Describe in natural language WHAT must be changed without referencing the exact old code.
Only return an empty plan if:
- The file name does not exist AND there is no provided code snippets.
Goal:
Your output will be consumed by a Code Generation Patch Agent that will apply the actual changes. Your job is only planning.

End of system instruction.

"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_context,
                response_mime_type="application/json",
            ),
            contents=prompt,
        )

       
        try:
            response = json.loads(response.text)
            current_state.patch_plan = response
            print("plan:=====>\n",response)
            return response
        except Exception:
            raise ValueError("PatchApplyAgent returned invalid JSON")
        
        
       
    


