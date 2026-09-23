import os
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


def configure_ssl():
    """Attempt to use the system certificate store when available.

    Some Windows/Python 3.14 installations fail when truststore is injected
    globally. In that case we fall back to the standard ssl configuration rather
    than crashing the process during import.
    """
    try:
        import truststore
    except ImportError:
        return False

    try:
        truststore.inject_into_ssl()
        return True
    except Exception:
        return False


configure_ssl()

APP_ENV = os.getenv("APP_ENV", "dev").strip().lower()
ENV_FILE = {
    "dev": "dev.env",
    "stage": "stage.env",
    "prod": "prod.env"
}.get(APP_ENV, "dev.env")

load_dotenv(BASE_DIR / "config" / ENV_FILE, override=False)

BASE_URL = "https://api.themoviedb.org/3"


def get_headers():
    token = os.getenv("TMDB_ACCESS_TOKEN", "").strip()
    if not token:
        raise ValueError("TMDB_ACCESS_TOKEN is missing. Set it in the environment or .env file.")

    return {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }


def get_movie(movie_id):
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}",
        headers=get_headers(),
        timeout=30
    )

    response.raise_for_status()
    return response.json()