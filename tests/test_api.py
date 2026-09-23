from unittest.mock import Mock, patch

from orchestrator.api_extractor import get_movie


@patch("orchestrator.api_extractor.requests.get")
def test_get_movie(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "id": 550,
        "title": "Fight Club"
    }
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    movie = get_movie(550)

    assert movie["id"] == 550
    assert movie["title"] == "Fight Club"

    mock_get.assert_called_once()