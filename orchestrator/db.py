import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "config" / "dev.env")

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "").strip(),
        port=os.getenv("DB_PORT", "").strip(),
        dbname=os.getenv("DB_NAME", "").strip(),
        user=os.getenv("DB_USER", "").strip(),
        password=os.getenv("DB_PASSWORD", "").strip(),
    )