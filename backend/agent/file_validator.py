
import json
from pydantic import ValidationError
from backend.agent.schema import FileSchema

class FileValidator:
    """
    Validates the raw LLM response. It:
    - Parses text → dict when needed
    - Validates structure using Pydantic
    - Returns True/False (for now)
    """

    @staticmethod
    def parse_llm_json(output: str | dict) -> dict:
        """
        Normalize LLM responses by ensuring they become valid Python dicts.
        """
        # Case 1: Already parsed
        if isinstance(output, dict):
            return output
        
        # Case 2: Try to parse JSON string
        try:
            return json.loads(output)
        except Exception:
            raise ValueError(" LLM did NOT return valid JSON.")

    @staticmethod
    def is_valid(raw_output: str | dict) -> bool:
        """
        Validate response by parsing then applying Pydantic schema.
        """
        try:
            parsed = FileValidator.parse_llm_json(raw_output)
            FileSchema(**parsed)  # Full schema validation
            return True
        except (ValueError, ValidationError):
            return False
