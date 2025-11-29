from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient
from google.genai import types


class PachPlanningAgent():
    def __init__(self):
        self.client = LLMClient().get()

    def run(self, user_prompt: str, code_snippets: str):
        prompt = f"""
USER REQUEST:
{user_prompt}

RELEVANT CODE SNIPPETS (from semantic search):
{code_snippets}

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

        
        return response.text
    


