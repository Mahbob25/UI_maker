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

You are NOT generating code. Only planning screens.

Output REQUIRED Format (STRICT):
- Output MUST be ONLY valid JSON.
- NO explanations or markdown.
- JSON MUST be:

{
  "app_name": "<short human readable app name>",
  "features": [
     { "name": "<canonical screen name>", "description": "<what user does on this screen>" }
  ]
}

RULES:
- Screen names MUST be short (max 3 words).
- One entry per UI screen.
- NO technical terms (no 'component', 'module', 'route', 'HTML', 'TS', 'CSS', etc.).
- DO NOT include file paths or file types.
- DO NOT include Angular concepts.

Your output MUST follow the structure above exactly.
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
        """Convert raw output into canonical Angular metadata + ordered file planning."""
        app_name = str(raw.get("app_name", "Generated App")).strip()
        raw_features: List[Dict[str, Any]] = raw.get("features", [])

        normalized_features = []
        seen = set()

        # ---------- Normalize Screen Features ----------
        for feat in raw_features:
            name = str(feat.get("name", "")).strip()
            desc = str(feat.get("description", "")).strip()

            if not name or name in seen:
                continue

            kebab = self._to_kebab_case(name)
            class_name = self._to_pascal_case(name) + "PageComponent"
            selector = f"app-{kebab}"
            file_name = f"{kebab}.page.ts"
            route = f"/{kebab}"

            normalized_features.append({
                "canonical_name": name,
                "description": desc,
                "selector": selector,
                "route": route,
                "file_name": file_name,
                "class_name": class_name,
            })

            seen.add(name)

        # ---------- Routing Metadata ----------
        default_redirect = ""
        if normalized_features:
            default_redirect = normalized_features[0]["route"].lstrip("/")

        routing = {
            "file_name": "app.routes.ts",
            "default_redirect": default_redirect
        }

        # ---------- Build Ordered File List ----------
        ordered_files: List[Dict[str, Any]] = []

        # For each feature → HTML → TS → CSS
        for feat in normalized_features:
            kebab = self._to_kebab_case(feat["canonical_name"])

            # HTML
            ordered_files.append({
                "type": "html",
                "path": f"src/app/{kebab}/{kebab}.page.html",
                "feature": feat["canonical_name"]
            })

            # CSS
            ordered_files.append({
                "type": "css",
                "path": f"src/app/{kebab}/{kebab}.page.css",
                "feature": feat["canonical_name"]
            })

             # TS
            ordered_files.append({
                "type": "ts",
                "path": f"src/app/{kebab}/{kebab}.page.ts",
                "feature": feat["canonical_name"]
            })

        # ---------- Add Routing + App Component Files (Always Last) ----------
        ordered_files.append({
            "type": "routing",
            "path": "src/app/app.routes.ts"
        })
        ordered_files.append({
            "type": "app_html",
            "path": "src/app/app.component.html"
        })
        ordered_files.append({
            "type": "app_ts",
            "path": "src/app/app.component.ts"
        })
        ordered_files.append({
            "type": "app_css",
            "path": "src/app/app.component.css"
        })

        # ---------- Final Plan ----------
        return {
            "app_name": app_name,
            "features": normalized_features,
            "routing": routing,
            "files": ordered_files
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
