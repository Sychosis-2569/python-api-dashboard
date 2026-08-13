from src.api_client import APIError, get_location_coordinates, get_weather
from src.dashboard import display_weather
from src.models import create_weather_data
from src.utils import configure_logging


def main() -> None:
    """Run the weather dashboard."""

    configure_logging()

    print("Python API Dashboard")
    print("--------------------")

    location = input("Enter a location: ").strip()

    if not location:
        print("Please enter a location.")
        return

    try:
        latitude, longitude = get_location_coordinates(location)

        weather_response = get_weather(latitude, longitude)

        weather = create_weather_data(weather_response)

        display_weather(location, weather)

    except ValueError as error:
        print(f"Error: {error}")

    except APIError as error:
        print(f"API Error: {error}")

    except Exception as error:
     print(f"An unexpected error occurred: {error}")
