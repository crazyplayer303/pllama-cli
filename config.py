# config.py

"""Configuration loader for PLLaMa CLI."""

from dotenv import load_dotenv
import os

# Load environment variables from a local .env file if present
load_dotenv()

API_URL = os.getenv("API_URL")
HF_TOKEN = os.getenv("HF_TOKEN")

if not API_URL or not HF_TOKEN:
    raise EnvironmentError(
        "API_URL and HF_TOKEN must be set in the environment"
    )
