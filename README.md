# Python API Dashboard

A command-line weather dashboard built with Python that retrieves live weather data from the Open-Meteo API.

The project demonstrates API integration, data modelling, error handling, logging, automated testing and modular Python architecture.

## Features

- Search for weather by city name
- Geocode locations using the Open-Meteo Geocoding API
- Retrieve current weather conditions
- Retrieve a five-day forecast
- Display temperature, humidity and wind speed
- Translate WMO weather codes into readable descriptions
- Handle invalid locations and API errors
- Structured data models using Python dataclasses
- Automated tests using pytest
- Modular project structure

## Technologies

- Python 3.11+
- Requests
- Pytest
- Open-Meteo API
- Git / GitHub

## Project Structure

```text
python-api-dashboard/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── api_client.py
│   ├── dashboard.py
│   ├── models.py
│   └── utils.py
│
└── tests/
    ├── test_api_client.py
    └── test_models.py