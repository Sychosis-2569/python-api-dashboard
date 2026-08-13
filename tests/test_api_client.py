import pytest
import requests
from unittest.mock import Mock, patch

from src.api_client import APIError, get_location_coordinates


@patch("src.api_client.requests.get")
def test_location_not_found(mock_get):
    """A missing location should raise ValueError."""

    mock_response = Mock()
    mock_response.json.return_value = {"results": []}

    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Location not found"):
        get_location_coordinates("NotARealPlace123")

@patch("src.api_client.requests.get")
def test_api_http_error(mock_get):
    """An HTTP error should be converted into APIError."""

    mock_response = Mock()

    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "API unavailable"
    )

    mock_get.return_value = mock_response

    with pytest.raises(APIError, match="Unable to retrieve location data"):
        get_location_coordinates("Pretoria")