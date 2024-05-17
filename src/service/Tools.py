import os

from dotenv import load_dotenv


class Tools:

    @staticmethod
    def get_openai_api_key():
        """Retrieve OpenAI API key from environment variable."""
        # Load environment variables from .env file
        load_dotenv()

        # Get the OpenAI API key from the environment variable
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key is None:
            raise ValueError("OpenAI API key not found. Make sure to set OPENAI_API_KEY in your environment.")

        return api_key

    @staticmethod
    def get_serper_api_key():
        """Retrieve Serper API key from environment variable."""
        # Load environment variables from .env file
        load_dotenv()

        # Get the OpenAI API key from the environment variable
        api_key = os.getenv("SERPER_API_KEY")

        if api_key is None:
            raise ValueError("SERPER API key not found. Make sure to set SERPER_API_KEY in your environment.")

        return api_key
