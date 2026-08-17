from unittest.mock import patch

from main import select_location
from src.models import Location


def test_select_location():
    """The selected location should match the user's choice."""

    locations = [
        Location(
            name="Cape Town",
            country="South Africa",
            admin1="Western Cape",
            latitude=-33.9258,
            longitude=18.4232,
        ),
        Location(
            name="Cape Townshend",
            country="Australia",
            admin1="Queensland",
            latitude=-20.0,
            longitude=146.0,
        ),
    ]

    with patch("builtins.input", return_value="2"):
        result = select_location(locations)

    assert result.name == "Cape Townshend"
    assert result.country == "Australia"
    assert result.latitude == -20.0
    assert result.longitude == 146.0


def test_select_location_rejects_invalid_input():
    """Invalid selections should prompt the user again."""

    locations = [
        Location(
            name="Pretoria",
            country="South Africa",
            admin1="Gauteng",
            latitude=-25.7449,
            longitude=28.1878,
        ),
        Location(
            name="Johannesburg",
            country="South Africa",
            admin1="Gauteng",
            latitude=-26.2023,
            longitude=28.0436,
        ),
    ]

    with patch(
        "builtins.input",
        side_effect=["banana", "99", "2"],
    ):
        result = select_location(locations)

    assert result.name == "Johannesburg"