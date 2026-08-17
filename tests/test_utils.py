from src.utils import get_weather_description
from src.utils import get_weather_description, normalize_location_input


def test_clear_sky_weather_code():
    """Weather code 0 should return 'Clear sky'."""

    result = get_weather_description(0)

    assert result == "Clear sky"


def test_unknown_weather_code():
    """An unknown weather code should return a fallback description."""

    result = get_weather_description(999)

    assert result == "Unknown conditions"

def test_normalize_location_input():
    """Location input should have unnecessary whitespace removed."""

    result = normalize_location_input("  Cape    Town  ")

    assert result == "Cape Town"


def test_normalize_location_input_preserves_normal_input():
    """Normal location input should remain unchanged."""

    result = normalize_location_input("Pretoria")

    assert result == "Pretoria"