from src.models import WeatherData
from src.utils import get_weather_description


def display_weather(location: str, weather: WeatherData) -> None:
    """Display current weather information in the terminal."""

    print()
    print("=" * 40)
    print(f"Weather for {location}")
    print("=" * 40)

    print(f"Temperature : {weather.temperature:.1f} °C")
    print(f"Humidity    : {weather.humidity}%")
    print(f"Wind Speed  : {weather.wind_speed:.1f} km/h")
    print(f"Conditions   : {get_weather_description(weather.weather_code)}")
    print(f"Time        : {weather.time}")
    print(f"Timezone    : {weather.timezone}")

    print("=" * 40)