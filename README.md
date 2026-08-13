# Python API Dashboard

A modular Python application that retrieves weather information from the Open-Meteo API and presents current conditions for a user-selected location.

## Features

- Search for locations using the Open-Meteo Geocoding API
- Retrieve current weather conditions
- Display temperature, humidity and wind speed
- Convert WMO weather codes into readable descriptions
- Handle invalid locations and API errors
- Application logging
- Automated tests using pytest
- Modular project architecture

## Technologies

- Python 3
- Requests
- pytest
- Open-Meteo API

## Project Structure

```text
python-api-dashboard/
│
├── src/
│   ├── api_client.py
│   ├── dashboard.py
│   ├── models.py
│   └── utils.py
│
├── tests/
│   ├── test_api_client.py
│   └── test_models.py
│
├── main.py
├── requirements.txt
└── .gitignore