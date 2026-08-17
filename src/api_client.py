import logging
import re

import requests

from src.models import Location, create_location_data
from src.utils import normalize_location_input


logger = logging.getLogger(__name__)


class APIError(Exception):
    """Raised when an API request fails."""


def _normalize_search_query(location: str) -> str:
    """Normalize a location search query."""

    query = location.strip().lower()

    # Collapse repeated whitespace.
    query = re.sub(r"\s+", " ", query)

    # Handle common cases where a city name is typed without a space.
    common_names = {
        "capetown": "cape town",
        "johannesburg": "johannesburg",
        "pretoria": "pretoria",
        "durban": "durban",
        "portelizabeth": "port elizabeth",
    }

    return common_names.get(query, query)


def _rank_locations(
    locations: list[Location],
    search_query: str,
) -> list[Location]:
    """Rank locations by how closely they match the search query."""

    query = _normalize_search_query(search_query)

    def score(location: Location) -> tuple[int, int]:
        name = location.name.lower()

        # Highest priority: exact city-name match.
        if name == query:
            match_score = 0

        # Next: city name starts with the search query.
        elif name.startswith(query):
            match_score = 1

        # Then: search query appears somewhere in the name.
        elif query in name:
            match_score = 2

        # Finally: unrelated API matches.
        else:
            match_score = 3

        # Prefer shorter names when the match quality is otherwise equal.
        return match_score, len(name)

    return sorted(locations, key=score)


def search_locations(location: str) -> list[Location]:
    """Return possible locations matching a search query."""

    query = _normalize_search_query(location)

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": query,
        "count": 5,
        "language": "en",
        "format": "json",
    }

    logger.info("Searching for location: %s", query)

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        logger.error("Location API request failed: %s", error)
        raise APIError("Unable to retrieve location data.") from error

    data = response.json()

    if not data.get("results"):
        raise ValueError(f"Location not found: {location}")

    locations = [
        create_location_data(result)
        for result in data["results"]
    ]

    return _rank_locations(locations, query)


def get_weather(latitude: float, longitude: float) -> dict:
    """Return current weather data for a set of coordinates."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "relative_humidity_2m",
            "wind_speed_10m",
            "precipitation",
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

def _normalize_search_query(location: str) -> str:
    """Normalize a location search query."""

    query = normalize_location_input(location).lower()

    common_names = {
        "capetown": "cape town",
        "johannesburg": "johannesburg",
        "pretoria": "pretoria",
        "durban": "durban",
        "portelizabeth": "port elizabeth",
    }

    return common_names.get(query, query)