import json
import re
from typing import List, Dict, Any
from google.genai import types
from backend.agent.registry import current_state
from backend.utils.llm_client import LLMClient


class FeatureExtractionAgent:
    """
    Step: Extract user-visible features (pages/screens) from spec_clean
    and convert them into normalized Angular page component file paths.

    Result is stored in:
        current_state.project_metadata.feature_files
    """

    SYSTEM_INSTRUCTION = """
You are a Feature Extraction Agent.

Your task:
- Read the product specification.
- Identify only user-visible screens/pages/views that the user will interact with.
- Ignore background services, utilities, APIs, or non-UI logic.
- Convert each screen into a short, clear feature name.

Output FORMAT RULES (IMPORTANT):
- You MUST output ONLY valid JSON.
- The JSON MUST be an array of objects.
- Each object MUST have:
    { "name": "<short feature name>", "description": "<what this screen does>" }
- DO NOT include any text before or after the JSON.
- DO NOT wrap the JSON in markdown code fences.
- Examples of valid output:

[
  {
    "name": "Login",
    "description": "Screen where users enter credentials to access their account."
  },
  {
    "name": "Dashboard Overview",
    "description": "Main overview showing key metrics and recent activity."
  }
]
"""

    def __init__(self) -> None:
        self.client = LLMClient.get()

    # ---------- Public API ----------

    def run(self) -> List[str]:
        """
        Reads spec_clean from state, calls LLM to extract features,
        normalizes them into file paths, stores them in metadata,
        and returns the final feature file list.
        """
        spec = current_state.spec_clean
        if not spec or not spec.strip():
            raise ValueError("FeatureExtractionAgent: spec_clean is empty; cannot extract features.")

        raw_features = self._call_llm(spec)
        file_paths = self._normalize_features(raw_features)

        # Fallback if nothing valid was extracted
        if not file_paths:
            file_paths = ["src/app/home.page.ts"]

        # Save into global state
        current_state.project_metadata.feature_files = file_paths

        
        return file_paths

    # ---------- Internal Helpers ----------

    def _call_llm(self, spec: str) -> List[Dict[str, Any]]:
        """
        Calls the LLM with spec_clean and returns a list of feature dicts:
        [{ "name": "...", "description": "..." }, ...]
        """
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=self.SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
            ),
            contents=spec,
        )

        text = response.text or ""

        # First attempt: direct JSON parse
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            # Fallback: try to extract JSON array between first '[' and last ']'
            data = self._extract_json_array(text)

        if not isinstance(data, list):
            return []

        features: List[Dict[str, Any]] = []
        for item in data:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", "")).strip()
            desc = str(item.get("description", "")).strip()
            if not name:
                continue
            features.append({"name": name, "description": desc})

        return features

    def _extract_json_array(self, text: str) -> Any:
        """
        Very small fallback to try to recover JSON if the model accidentally
        returns extra text. Not meant to be perfect, just resilient.
        """
        start = text.find("[")
        end = text.rfind("]")
        if start == -1 or end == -1 or end <= start:
            return []
        snippet = text[start : end + 1]
        try:
            return json.loads(snippet)
        except json.JSONDecodeError:
            return []

    def _normalize_features(self, raw_features: List[Dict[str, Any]]) -> List[str]:
        """
        Convert feature names to Angular page component file paths:
        - Name → kebab-case
        - File path: src/app/<kebab>.page.ts
        - Ensure uniqueness
        - Avoid conflicts with base_files
        """
        base_files = set(current_state.project_metadata.base_files or [])
        seen: set[str] = set()
        file_paths: List[str] = []

        for feat in raw_features:
            name = feat.get("name", "")
            if not name:
                continue

            kebab = self._to_kebab_case(name)
            if not kebab:
                continue

            path = f"src/app/{kebab}.page.ts"

            # Skip if clashes with base files or already added
            if path in base_files or path in seen:
                continue

            seen.add(path)
            file_paths.append(path)

        return file_paths

    def _to_kebab_case(self, name: str) -> str:
        """
        Convert arbitrary feature names to kebab-case:
          "User Profile" -> "user-profile"
          "DashboardOverview" -> "dashboard-overview"
          "  login  " -> "login"
        """
        # Remove non-alphanumeric except spaces and hyphens
        cleaned = re.sub(r"[^a-zA-Z0-9\s\-]", " ", name)
        # Split camelCase / PascalCase boundaries with spaces
        cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", cleaned)

        parts = [p.lower() for p in cleaned.split() if p.strip()]
        return "-".join(parts)
