import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app_env = os.getenv("APP_ENV", "dev")
env_file = BASE_DIR / "config" / f"{app_env}.env"

load_dotenv(env_file, override=False)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "").strip(),
        port=os.getenv("DB_PORT", "").strip(),
        dbname=os.getenv("DB_NAME", "").strip(),
        user=os.getenv("DB_USER", "").strip(),
        password=os.getenv("DB_PASSWORD", "").strip(),
    )