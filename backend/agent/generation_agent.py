from backend.utils.system_context_builder import SystemContextBuilder
from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient
from google.genai import types


class GenerationAgent:
    """
    Generates a single file based on the current project's context and feature plan.
    It calls the LLM once, returns a JSON object of the shape:
        { "path": "<file_path>", "content": "<full file source>" }
    and stores the raw JSON string into current_state.files_json_raw[file_path].

    This agent does NOT validate or fix the JSON; that is handled by later steps.
    """

    def __init__(self) -> None:
        self.client = LLMClient.get()
        self.context_builder = SystemContextBuilder()

    def generate(self, file_path: str) -> str:
        """
        Generate a single file for the given file_path.

        Requirements:
        - PromptEngineeringAgent + FeaturePlanningAgent must have already run.
        - current_state.feature_plan must be populated.
        - spec_clean should not be empty (used earlier to derive the plan).
        """
        spec = current_state.spec_clean

        if not spec or not spec.strip():
            raise ValueError(
                "GenerationAgent: spec_clean is empty. "
                "Run PromptEngineeringAgent and FeaturePlanningAgent first."
            )

        if not file_path or not file_path.strip():
            raise ValueError("GenerationAgent: file_path cannot be empty.")

        # Build and store the system context (includes feature_plan JSON)
        system_context = self.context_builder.build()
        current_state.system_context = system_context

        # Detect if we are generating the routing file or a page component
        is_routing_file = file_path.endswith("app.routes.ts")

        # ---------- Build user prompt ----------
        base_prompt = f"""
Generate ONLY the TypeScript code for this single file.

Target file path:
{file_path}

Global Rules:
- Follow the FEATURE PLAN and system rules provided in the system context.
- The output MUST be valid JSON with the exact shape:
  {{
    "path": "<file path>",
    "content": "<full TypeScript source code>"
  }}

# FILE PATH RULES
- The JSON field "path" MUST be exactly "{file_path}".
- Do NOT change file name, folder, extension, or prefix.
- Do NOT add, prepend, or concatenate ANY extra path text.
- If unsure, always use exactly: "{file_path}".
- Generate code for ONLY this file. Do NOT generate multiple files.
- Do NOT include explanations, comments, markdown, or backticks outside the JSON.
"""

        if is_routing_file:
            # Extra instructions specific to app.routes.ts
            role_specific = f"""
Routing-specific rules:
- Use Angular {current_state.project_metadata.angular_version} standalone routing.
- Build the routes array ONLY from the FEATURE PLAN.
- For each feature in the FEATURE PLAN:
  - Use its "route" value, but WITHOUT the leading slash as the path.
  - Load the component lazily from "./<file_name_without_extension>".
  - Use the exact "class_name" from the FEATURE PLAN in the lazy import.
- Use the "default_redirect" from the FEATURE PLAN routing section for:
  {{ path: '', redirectTo: '<default_redirect>', pathMatch: 'full' }}
"""
        else:
            # Page component rules: must map to a feature in the plan
            role_specific = f"""
Component-specific rules:
- Treat this file as a standalone Angular page component.
- Find the feature in the FEATURE PLAN whose "file_name" matches the basename of "{file_path}".
- Use its "class_name" EXACTLY as the component class name.
- Use its "selector" EXACTLY as the @Component selector.
- Use inline template (template property) and inline styles (styles property).
- ALWAYS import CommonModule.
- Import RouterLink if routerLink is used in the template.
- Import RouterOutlet if the component hosts nested routed content.
"""

        user_prompt = base_prompt + role_specific

        # ---------- Call LLM ----------
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_context,
                response_mime_type="application/json",
            ),
            contents=user_prompt,
        )

        raw_text = response.text or ""

        # Ensure dict is initialized
        if current_state.files_json_raw is None:
            current_state.files_json_raw = {}

        # Store raw output WITHOUT validation (handled later)
        current_state.files_json_raw[file_path] = raw_text.strip()

        return raw_text  # raw JSON string from the LLM







