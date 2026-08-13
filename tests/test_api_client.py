import pytest
import requests
from unittest.mock import Mock, patch

from src.api_client import APIError, get_location_coordinates, get_weather


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


@patch("src.api_client.requests.get")
def test_get_weather_success(mock_get):
    """A successful weather request should return the API response."""

    mock_response = Mock()
    mock_response.json.return_value = {
        "timezone": "Africa/Johannesburg",
        "current": {
            "temperature_2m": 15.4,
            "relative_humidity_2m": 44,
            "wind_speed_10m": 2.7,
            "weather_code": 0,
            "time": "2026-08-13T16:45",
        },
    }

    mock_get.return_value = mock_response

    result = get_weather(-25.7449, 28.1878)

    assert result["timezone"] == "Africa/Johannesburg"
    assert result["current"]["temperature_2m"] == 15.4

    mock_get.assert_called_once()


@patch("src.api_client.requests.get")
def test_weather_api_http_error(mock_get):
    """A weather API HTTP error should be converted into APIError."""

    mock_response = Mock()

    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "API unavailable"
    )

    mock_get.return_value = mock_response

    with pytest.raises(APIError, match="Unable to retrieve weather data"):
        get_weather(-25.7449, 28.1878)