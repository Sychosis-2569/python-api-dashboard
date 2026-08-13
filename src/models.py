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


@dataclass
class ForecastDay:
    """Represents a single day in the weather forecast."""

    date: str
    weather_code: int
    temperature_max: float
    temperature_min: float


def create_forecast_data(api_response: dict) -> list[ForecastDay]:
    """Convert an Open-Meteo daily forecast into ForecastDay objects."""

    daily = api_response["daily"]

    return [
        ForecastDay(
            date=date,
            weather_code=weather_code,
            temperature_max=temperature_max,
            temperature_min=temperature_min,
        )
        for date, weather_code, temperature_max, temperature_min in zip(
            daily["time"],
            daily["weather_code"],
            daily["temperature_2m_max"],
            daily["temperature_2m_min"],
        )
    ]