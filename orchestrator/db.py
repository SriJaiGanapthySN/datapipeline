import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

APP_ENV = os.getenv("APP_ENV", "dev").strip().lower()
ENV_FILE = {
    "dev": "dev.env",
    "stage": "stage.env",
    "prod": "prod.env",
}.get(APP_ENV, "dev.env")

load_dotenv(BASE_DIR / "config" / ENV_FILE, override=False)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "").strip(),
        port=os.getenv("DB_PORT", "").strip(),
        dbname=os.getenv("DB_NAME", "").strip(),
        user=os.getenv("DB_USER", "").strip(),
        password=os.getenv("DB_PASSWORD", "").strip(),
    )