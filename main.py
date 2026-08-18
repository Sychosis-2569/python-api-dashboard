from src.api_client import APIError, get_weather, search_locations
from src.dashboard import display_forecast, display_weather
from src.models import Location, create_forecast_data, create_weather_data
from src.utils import configure_logging, normalize_location_input

def select_location(results: list[Location]) -> Location:
    """Allow the user to select a location from search results."""

    if len(results) == 1:
        return results[0]

    print("\nMultiple locations found:")

    for index, result in enumerate(results, start=1):
        if result.admin1:
            print(f"{index}. {result.name}, {result.admin1}, {result.country}")
        else:
            print(f"{index}. {result.name}, {result.country}")

    while True:
        choice = input(
            f"\nSelect a location (1-{len(results)}): "
        ).strip()

        try:
            selection = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= selection <= len(results):
            return results[selection - 1]

        print(f"Please choose a number between 1 and {len(results)}.")


def display_location_weather(location: str) -> None:
    """Fetch and display weather information for a location."""

    try:
        locations = search_locations(location)
        selected_location = select_location(locations)

        latitude = selected_location.latitude
        longitude = selected_location.longitude

        display_name = selected_location.name

        weather_response = get_weather(latitude, longitude)

        weather = create_weather_data(weather_response)
        forecast = create_forecast_data(weather_response)

        display_weather(display_name, weather)
        display_forecast(forecast)

    except ValueError as error:
        print(f"Error: {error}")

    except APIError as error:
        print(f"API Error: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def main() -> None:
    """Run the weather dashboard."""

    configure_logging()

    print("Python API Dashboard")
    print("--------------------")

    try:
        while True:
            location = input(
                "\nEnter a location (or press Enter to exit): "
            )

            location = normalize_location_input(location)

            if not location:
                print("Goodbye!")
                break

            display_location_weather(location)

    except KeyboardInterrupt:
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()