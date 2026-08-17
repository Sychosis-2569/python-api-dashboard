from dataclasses import dataclass

@dataclass
class Location:
    """Represents a geocoded location."""

    name: str
    country: str
    admin1: str | None
    latitude: float
    longitude: float

def create_location_data(api_response: dict) -> Location:
    """Convert a geocoding API result into a Location object."""

    return Location(
        name=api_response["name"],
        country=api_response["country"],
        admin1=api_response.get("admin1"),
        latitude=api_response["latitude"],
        longitude=api_response["longitude"],
    )


@dataclass
class WeatherData:
    """Represents the current weather conditions for a location."""

    temperature: float
    apparent_temperature: float
    humidity: int
    wind_speed: float
    precipitation: float
    weather_code: int
    time: str
    timezone: str


def create_weather_data(api_response: dict) -> WeatherData:
    """Convert an Open-Meteo API response into a WeatherData object."""

    current = api_response["current"]

    return WeatherData(
        temperature=current["temperature_2m"],
        apparent_temperature=current["apparent_temperature"],
        humidity=current["relative_humidity_2m"],
        wind_speed=current["wind_speed_10m"],
        precipitation=current["precipitation"],
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