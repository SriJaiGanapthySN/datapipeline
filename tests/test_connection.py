from unittest.mock import patch, Mock
from orchestrator.db import get_connection


@patch("orchestrator.db.psycopg2.connect")
def test_get_connection(mock_connect):

    fake_connection = Mock()
    mock_connect.return_value = fake_connection

    conn = get_connection()

    assert conn == fake_connection
    mock_connect.assert_called_once()