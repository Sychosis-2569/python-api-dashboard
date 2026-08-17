from src.models import (
    ForecastDay,
    Location,
    WeatherData,
    create_forecast_data,
    create_location_data,
    create_weather_data,
)

def test_create_weather_data():
    """API data should be converted into a WeatherData object."""

    api_response = {
        "timezone": "Africa/Johannesburg",
        "current": {
            "temperature_2m": 15.3,
            "apparent_temperature": 14.8,
            "relative_humidity_2m": 44,
            "precipitation": 0.0,
            "wind_speed_10m": 4.6,
            "weather_code": 0,
            "time": "2026-08-13T13:15",
        },
    }

    weather = create_weather_data(api_response)

    assert isinstance(weather, WeatherData)
    assert weather.temperature == 15.3
    assert weather.apparent_temperature == 14.8
    assert weather.humidity == 44
    assert weather.precipitation == 0.0
    assert weather.wind_speed == 4.6
    assert weather.weather_code == 0
    assert weather.time == "2026-08-13T13:15"
    assert weather.timezone == "Africa/Johannesburg"


def test_create_forecast_data():
    """Daily API data should be converted into ForecastDay objects."""

    api_response = {
        "daily": {
            "time": [
                "2026-08-13",
                "2026-08-14",
            ],
            "weather_code": [
                3,
                0,
            ],
            "temperature_2m_max": [
                15.8,
                18.5,
            ],
            "temperature_2m_min": [
                4.8,
                4.8,
            ],
        }
    }

    forecast = create_forecast_data(api_response)

    assert len(forecast) == 2
    assert isinstance(forecast[0], ForecastDay)

    assert forecast[0].date == "2026-08-13"
    assert forecast[0].weather_code == 3
    assert forecast[0].temperature_max == 15.8
    assert forecast[0].temperature_min == 4.8

    assert forecast[1].date == "2026-08-14"
    assert forecast[1].weather_code == 0
    assert forecast[1].temperature_max == 18.5
    assert forecast[1].temperature_min == 4.8

def test_create_location_data():
    """Geocoding API data should be converted into a Location object."""

    api_response = {
        "name": "Cape Town",
        "country": "South Africa",
        "admin1": "Western Cape",
        "latitude": -33.9258,
        "longitude": 18.4232,
    }

    location = create_location_data(api_response)

    assert isinstance(location, Location)
    assert location.name == "Cape Town"
    assert location.country == "South Africa"
    assert location.admin1 == "Western Cape"
    assert location.latitude == -33.9258
    assert location.longitude == 18.4232


def test_create_location_data_without_region():
    """Location data should support missing regional information."""

    api_response = {
        "name": "Somewhere",
        "country": "Test Country",
        "latitude": 10.0,
        "longitude": 20.0,
    }

    location = create_location_data(api_response)

    assert isinstance(location, Location)
    assert location.name == "Somewhere"
    assert location.country == "Test Country"
    assert location.admin1 is None
    assert location.latitude == 10.0
    assert location.longitude == 20.0