import os
from dotenv import load_dotenv
from google import genai

class LLMClient:
    """This class prepare the API key and get the google client"""
    _instance = None

    @staticmethod
    def get():
        """Singleton Google Gemini client"""
        if LLMClient._instance is None:
            load_dotenv()
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY is missing in .env")
            LLMClient._instance = genai.Client(api_key=api_key)
        return LLMClient._instance
