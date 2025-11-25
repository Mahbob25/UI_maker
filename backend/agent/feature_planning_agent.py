import json
import re
from typing import List, Dict, Any
from google.genai import types
from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient


class FeaturePlanningAgent:
    """
    Step: Read spec_clean -> Extract UI features (names + descriptions)
    -> Build canonical Angular naming plan (routes, selectors, class names)
    -> Add routing info including default redirect
    -> Save full planning JSON into state.feature_plan

    Does NOT generate code. Only planning.
    """

    SYSTEM_INSTRUCTION = """
You are a Feature Planning Agent.

Your task:
- Read the product specification (text-based).
- Identify ONLY user-visible pages/screens that the user interacts with.
- Ignore backend logic, APIs, state management, or background processes.

Output Purpose:
We are planning UI screens. We are NOT generating Angular code.

Output REQUIRED Format (STRICT):
- You MUST output ONLY valid JSON.
- Do NOT include explanations or markdown.
- The JSON MUST be:
{
  "app_name": "<short human readable app name>",
  "features": [
     { "name": "<canonical screen name>", "description": "<what user does on this screen>" }
  ]
}

Naming Rules:
- Screen names MUST be short (max 3 words).
- Keep naming consistent (e.g., use “Resume Editor” instead of multiple synonyms).
- Do NOT mention technical concepts like modules, components, services, routes, or Angular.
"""

    def __init__(self) -> None:
        self.client = LLMClient.get()

    # ---------- Public API ----------

    def run(self) -> Dict[str, Any]:
        """
        1. Call LLM to extract app name + UI screens
        2. Normalize names into Angular naming scheme
        3. Add routing metadata
        4. Save into global state
        """
        spec = current_state.spec_clean
        if not spec or not spec.strip():
            raise ValueError("FeaturePlanningAgent: spec_clean is empty; cannot extract planning.")

        raw_plan = self._call_llm(spec)
        planning_json = self._normalize_plan(raw_plan)

        current_state.feature_plan = planning_json
        return planning_json

    # ---------- Internal Helpers ----------

    def _call_llm(self, spec: str) -> Dict[str, Any]:
        """Calls LLM to get app name + features."""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=self.SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
            ),
            contents=spec,
        )

        text = response.text or ""
        try:
            return json.loads(text)
        except Exception:
            return {}

    def _normalize_plan(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """Convert raw output into canonical Angular metadata."""
        app_name = str(raw.get("app_name", "Generated App")).strip()
        raw_features: List[Dict[str, Any]] = raw.get("features", [])

        normalized_features = []
        seen = set()

        for feat in raw_features:
            name = str(feat.get("name", "")).strip()
            desc = str(feat.get("description", "")).strip()

            if not name or name in seen:
                continue

            kebab = self._to_kebab_case(name)
            class_name = self._to_pascal_case(name) + "PageComponent"
            selector = f"app-{kebab}"
            file_name = f"{kebab}.page.ts"
            route = f"/{kebab}"  # stored with slash, but routing file will remove slash

            normalized_features.append({
                "canonical_name": name,
                "description": desc,
                "selector": selector,
                "route": route,                # stored normalized
                "file_name": file_name,
                "class_name": class_name,
            })

            seen.add(name)

        # ----------- Routing Metadata -----------
        default_redirect = ""
        if normalized_features:
            # remove slash for Angular redirect
            default_redirect = normalized_features[0]["route"].lstrip("/")

        routing = {
            "file_name": "app.routes.ts",
            "default_redirect": default_redirect
        }

        return {
            "app_name": app_name,
            "features": normalized_features,
            "routing": routing
        }

    # ---------- Naming Helpers ----------

    def _to_kebab_case(self, name: str) -> str:
        cleaned = re.sub(r"[^a-zA-Z0-9\s\-]", " ", name)
        cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", cleaned)
        parts = [p.lower() for p in cleaned.split() if p.strip()]
        return "-".join(parts)

    def _to_pascal_case(self, name: str) -> str:
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", " ", name)
        parts = [p.capitalize() for p in cleaned.split() if p.strip()]
        return "".join(parts)
