import os
from pathlib import Path

import certifi
import requests
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "config" / "dev.env")

BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('TMDB_ACCESS_TOKEN')}",
    "accept": "application/json"
}

def get_movie(movie_id):
    response = requests.get(
        f"{BASE_URL}/movie/{movie_id}",
        headers=HEADERS,
        verify=certifi.where(),   # Uses trusted CA bundle
        timeout=30
    )

    response.raise_for_status()
    return response.json()