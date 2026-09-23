from unittest.mock import Mock, patch

from orchestrator.api_extractor import configure_ssl, get_movie


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


@patch("truststore.inject_into_ssl")
def test_configure_ssl_handles_injection_failures(mock_inject):
    mock_inject.side_effect = RuntimeError("SSL injection failed")

    result = configure_ssl()

    assert result is False
    mock_inject.assert_called_once()