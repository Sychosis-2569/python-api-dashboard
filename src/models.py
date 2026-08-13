from dataclasses import dataclass


@dataclass
class WeatherData:
    """Represents the current weather conditions for a location."""

    temperature: float
    humidity: int
    wind_speed: float
    weather_code: int
    time: str
    timezone: str


def create_weather_data(api_response: dict) -> WeatherData:
    """Convert an Open-Meteo API response into a WeatherData object."""

    current = api_response["current"]

    return WeatherData(
        temperature=current["temperature_2m"],
        humidity=current["relative_humidity_2m"],
        wind_speed=current["wind_speed_10m"],
        weather_code=current["weather_code"],
        time=current["time"],
        timezone=api_response["timezone"],
    )