from src.models import ForecastDay, WeatherData
from src.utils import get_weather_description


def display_weather(location: str, weather: WeatherData) -> None:
    """Display the current weather conditions."""

    print()
    print("=" * 44)
    print(f"Weather for {location}")
    print("=" * 44)

    print(f"Temperature  : {weather.temperature:.1f} °C")
    print(f"Feels like   : {weather.apparent_temperature:.1f} °C")
    print(f"Humidity     : {weather.humidity}%")
    print(f"Wind Speed   : {weather.wind_speed:.1f} km/h")
    print(f"Precipitation: {weather.precipitation:.1f} mm")
    print(f"Conditions  : {get_weather_description(weather.weather_code)}")
    print(f"Time        : {weather.time}")
    print(f"Timezone    : {weather.timezone}")

    print("=" * 44)


def display_forecast(forecast: list[ForecastDay]) -> None:
    """Display the five-day weather forecast."""

    print()
    print("5-DAY FORECAST")
    print("-" * 64)
    print(f"{'Date':<12}{'Conditions':<20}{'High':>10}{'Low':>10}")
    print("-" * 64)

    for day in forecast:
        description = get_weather_description(day.weather_code)

        print(
            f"{day.date:<12}"
            f"{description:<20}"
            f"{day.temperature_max:>9.1f}°C"
            f"{day.temperature_min:>9.1f}°C"
        )

    print("-" * 64)