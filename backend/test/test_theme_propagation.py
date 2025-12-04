import json
import unittest

from backend.agent.registry import current_state
from backend.agent.feature_planning_agent import FeaturePlanningAgent
from backend.themes.themes import THEMES
from backend.utils.system_context_builder import SystemContextBuilder


class ThemePropagationTest(unittest.TestCase):

    def setUp(self):
        """Reset state before each test."""
        current_state.feature_plan = None
        current_state.user_selected_theme = None
        current_state.auto_theme_enabled = True
        current_state.project_metadata.angular_version = "19"

    # ----------------------------------
    # 1) TEST: Planner theme is used when auto_theme_enabled = True
    # ----------------------------------
    def test_planner_theme_used(self):
        current_state.spec_clean = "Build a modern dashboard application."

        # Mock planning output (simulating LLM result)
        raw_planner_output = {
            "app_name": "My Dashboard",
            "theme": "dark",
            "features": [
                {"name": "Home", "description": "Main screen"},
                {"name": "Reports", "description": "Shows analytics charts"}
            ]
        }

        agent = FeaturePlanningAgent()
        normalized = agent._normalize_plan(raw_planner_output)

        self.assertEqual(normalized["theme"], "dark")
        print("✔ Planner theme correctly applied:", normalized["theme"])

    # ----------------------------------
    # 2) TEST: User-selected theme overrides planner
    # ----------------------------------
    def test_user_theme_override(self):
        current_state.spec_clean = "A resume builder application."
        current_state.user_selected_theme = "lavender"
        current_state.auto_theme_enabled = True

        raw_planner_output = {
            "app_name": "Resume App",
            "theme": "dark",  # planner tries "dark"
            "features": [
                {"name": "Editor", "description": "Edit resume"},
            ]
        }

        agent = FeaturePlanningAgent()
        normalized = agent._normalize_plan(raw_planner_output)

        self.assertEqual(normalized["theme"], "lavender")
        print("✔ User-selected theme overrides planner:", normalized["theme"])

    # ----------------------------------
    # 3) TEST: auto_theme_enabled=False ignores planner theme
    # ----------------------------------
    def test_auto_theme_disabled(self):
        current_state.spec_clean = "A finance dashboard."
        current_state.auto_theme_enabled = False  # planner not allowed to choose

        raw_planner_output = {
            "app_name": "Finance App",
            "theme": "glacier",  # LLM suggests "glacier"
            "features": [
                {"name": "Charts", "description": "Financial charts"},
            ]
        }

        agent = FeaturePlanningAgent()
        normalized = agent._normalize_plan(raw_planner_output)

        self.assertEqual(normalized["theme"], "default")
        print("✔ auto_theme_enabled=False forces default:", normalized["theme"])

    # ----------------------------------
    # 4) TEST: Invalid planner theme → fallback default
    # ----------------------------------
    def test_invalid_planner_theme(self):
        current_state.spec_clean = "A shop application."
        current_state.auto_theme_enabled = True

        raw_planner_output = {
            "app_name": "Shop App",
            "theme": "alien",  # invalid theme name
            "features": [
                {"name": "Store", "description": "Browse items"}
            ]
        }

        agent = FeaturePlanningAgent()
        normalized = agent._normalize_plan(raw_planner_output)

        self.assertEqual(normalized["theme"], "default")
        print("✔ Invalid planner theme gracefully resets to default")

    # ----------------------------------
    # 5) TEST: SystemContextBuilder correctly injects theme details
    # ----------------------------------
    def test_system_context_theme_injection(self):
        current_state.feature_plan = {
            "app_name": "Demo",
            "theme": "glacier",
            "features": [],
            "routing": {},
            "files": []
        }

        builder = SystemContextBuilder()
        context = builder.build()

        # Expect theme tokens to be inside system context
        self.assertIn(THEMES["glacier"]["bg_page"], context)
        self.assertIn(THEMES["glacier"]["accent_bg"], context)
        self.assertIn("ACTIVE THEME", context)

        print("✔ SystemContextBuilder injected theme details successfully")



if __name__ == "__main__":
    unittest.main()
