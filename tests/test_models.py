from src.utils import get_weather_description


def test_clear_sky_weather_code():
    """Weather code 0 should return 'Clear sky'."""

    result = get_weather_description(0)

    assert result == "Clear sky"

from src.models import WeatherData, create_weather_data


def test_create_weather_data():
    """API data should be converted into a WeatherData object."""

    api_response = {
        "timezone": "Africa/Johannesburg",
        "current": {
            "temperature_2m": 15.3,
            "relative_humidity_2m": 44,
            "wind_speed_10m": 4.6,
            "weather_code": 0,
            "time": "2026-08-13T13:15",
        },
    }

    weather = create_weather_data(api_response)

    assert isinstance(weather, WeatherData)
    assert weather.temperature == 15.3
    assert weather.humidity == 44
    assert weather.wind_speed == 4.6
    assert weather.weather_code == 0
    assert weather.time == "2026-08-13T13:15"
    assert weather.timezone == "Africa/Johannesburg"