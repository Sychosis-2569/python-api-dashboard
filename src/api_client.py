from typing import Any

import logging

import requests


logger = logging.getLogger(__name__)

class APIError(Exception):
    """Raised when an API request fails."""


def search_locations(location: str) -> list[dict[str, Any]]:
    """Return possible locations matching a search query."""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": location,
        "count": 5,
        "language": "en",
        "format": "json",
    }

    logger.info("Searching for location: %s", location)

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        logger.error("Location API request failed: %s", error)
        raise APIError("Unable to retrieve location data.") from error

    data = response.json()

    if not data.get("results"):
        raise ValueError(f"Location not found: {location}")

    return data["results"]


def get_weather(latitude: float, longitude: float) -> dict:
    """Return current weather data for a set of coordinates."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "weather_code",
        ],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
        ],
        "forecast_days": 5,
        "timezone": "auto",
    }

    logger.info(
        "Requesting weather data for coordinates: %.4f, %.4f",
        latitude,
        longitude,
    )

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        logger.error("Weather API request failed: %s", error)
        raise APIError("Unable to retrieve weather data.") from error

    return response.json()