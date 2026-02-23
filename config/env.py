import os
from dotenv import load_dotenv

def load_environment() -> None:
    """Load environment variables from .env file and validate required keys."""
    load_dotenv()

    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError(
            "GOOGLE_API_KEY not found. Please create a .env file with your API key."
        )
