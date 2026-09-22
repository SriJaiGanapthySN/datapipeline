from unittest.mock import patch, Mock
from orchestrator.api_extractor import get_movie


@patch("orchestrator.api_extractor.requests.get")
def test_get_movie(mock_get):

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 550,
        "title": "Fight Club",
        "runtime": 139,
        "vote_average": 8.8
    }

    mock_get.return_value = fake_response

    movie = get_movie(550)

    assert movie["id"] == 550
    assert movie["title"] == "Fight Club"
    assert movie["runtime"] == 139