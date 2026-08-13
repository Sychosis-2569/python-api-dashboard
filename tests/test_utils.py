from src.utils import get_weather_description


def test_clear_sky_weather_code():
    """Weather code 0 should return 'Clear sky'."""

    result = get_weather_description(0)

    assert result == "Clear sky"


def test_unknown_weather_code():
    """An unknown weather code should return a fallback description."""

    result = get_weather_description(999)

    assert result == "Unknown conditions"