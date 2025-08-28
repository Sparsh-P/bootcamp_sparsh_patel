import os
from dotenv import load_dotenv


def load_secrets():
    """Load environment variables from .env file."""
    load_dotenv()
    print("Secrets loaded.")


def get_key(key_name='API_KEY'):
    """Fetch a specific key from the environment variables."""
    return os.getenv(key_name)