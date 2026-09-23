import os
from pathlib import Path

import truststore
truststore.inject_into_ssl()

import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

APP_ENV = os.getenv("APP_ENV", "dev")

ENV_FILE = {
    "dev": "dev.env",
    "stage": "stage.env",
    "prod": "prod.env"
}[APP_ENV]

load_dotenv(BASE_DIR / "config" / ENV_FILE)

BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('TMDB_ACCESS_TOKEN')}",
    "accept": "application/json"
}

def get_movie(movie_id):
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}",
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()
    return response.json()