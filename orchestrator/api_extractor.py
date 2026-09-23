import os
from pathlib import Path

import certifi
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "config" / "dev.env")

BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {os.getenv('TMDB_ACCESS_TOKEN')}",
    "Accept": "application/json"
}

# Create a reusable session with retries
session = requests.Session()

retries = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)
session.mount("http://", adapter)

def get_movie(movie_id):
    response = session.get(
        f"{BASE_URL}/movie/{movie_id}",
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()
    return response.json()