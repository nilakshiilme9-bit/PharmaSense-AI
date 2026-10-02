import sqlite3
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# PharmaSense database
DATABASE_PATH = BASE_DIR / "pharmasense.db"


def get_connection():
    """Create and return a connection to the PharmaSense database."""
    return sqlite3.connect(DATABASE_PATH)