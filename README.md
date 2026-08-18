# Python API Dashboard

A command-line weather dashboard built with Python that retrieves live weather data from the Open-Meteo API.

The project demonstrates practical Python development skills including REST API integration, data modelling with dataclasses, input validation, error handling, logging, automated testing, and modular application architecture.

## Features

- Search for locations by city name
- Normalize user location input
- Rank location search results by relevance
- Select from multiple matching locations
- Retrieve live weather conditions
- Display:
  - Temperature
  - Feels-like temperature
  - Humidity
  - Wind speed
  - Precipitation
  - Weather conditions
  - Local time
  - Timezone
- Display a five-day weather forecast
- Convert WMO weather codes into readable descriptions
- Handle invalid locations gracefully
- Handle API and network errors
- Gracefully handle Ctrl+C interruption
- Structured data models using Python dataclasses
- Logging for API operations
- Automated unit tests using pytest
- Mocked API requests for reliable testing
- Modular project structure

## Technologies

- **Python 3.11+**
- **Requests** - HTTP/API communication
- **Pytest** - automated testing
- **Open-Meteo API** - weather and geocoding data
- **Dataclasses** - structured application models
- **Logging** - application diagnostics
- **Git / GitHub** - version control

## APIs

This project uses the free Open-Meteo services:

- Open-Meteo Geocoding API - converts city names into geographic coordinates
- Open-Meteo Forecast API - retrieves current weather and forecast data

No API key is required.

## Project Structure

```text
python-api-dashboard/
|
+-- main.py
+-- requirements.txt
+-- README.md
+-- .gitignore
|
+-- src/
|   +-- api_client.py
|   +-- dashboard.py
|   +-- models.py
|   +-- utils.py
|
+-- tests/
    +-- test_api_client.py
    +-- test_main.py
    +-- test_models.py
    +-- test_utils.py