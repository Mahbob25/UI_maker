from backend.agent.llm_client import LLMClient
from google.genai import types
from .registry import current_state


class PromptEngineeringAgent:
    """This class improves the user prompt"""
    def __init__(self):
        self.client = LLMClient.get()
        self.system_instruction = """
You are a Prompt Engineering Specification Agent.

Your task:
Convert a messy user request into a clear, professional, and creative product specification,
without choosing specific technologies, libraries, frameworks, design systems, or implementation details.

Your output must focus on WHAT the solution should achieve, not HOW to build it.

# Required Output Structure:
1) **Core Functional Requirements**
2) **User Experience & Usability**
3) **Non-Functional Requirements**
4) **Accessibility & Inclusivity**
5) **Content & Messaging Considerations**
6) **Success Criteria**

# Rules:
- Do NOT mention tools (e.g., Angular, HTML, React, Node, database names, APIs, cloud, etc.)
- Write concise, requirement-style bullet points.
- Use professional, creative wording.
- Think beyond UI elements: consider behavior, validation, feedback, and constraints.
- The output must be only the improved prompt; do not ask questions or add explanations.
- If the user mentions specific technologies (e.g., HTML, CSS, JavaScript, React, Python, APIs, MySQL, etc.), ignore them and focus only on the underlying user intent. Convert the request into a technology-neutral specification without referencing any tool or implementation method.
- When the user request appears simple or UI-only, produce a concise version with no more than 5 sections and no section longer than 4 bullet points.

"""


    def run(self, prompt: str | None = None): # I added an optional prompt arg for testing purposes.
        """Transform raw prompt into structured spec and store it."""
        prompt = prompt or current_state.raw_user_prompt
        if not prompt or prompt.strip() == "":
            raise ValueError("Cannot run Prompt Engineering: raw_user_prompt is empty")

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=self.system_instruction),
            contents=prompt,
        )

        # Save in state memory
        current_state.spec_clean = response.text
        return response.text
