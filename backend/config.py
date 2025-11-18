import os
from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLite DB path
DB_PATH = BASE_DIR / "study_history.db"

# OpenAI API from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.4

SYSTEM_MESSAGE = (
    "You are a helpful AI study assistant for students at "
    "Metropolia University of Applied Sciences."
)