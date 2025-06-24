import pytest
from unitflex.core import convert

def test_valid_temperature_conversion():
    assert convert("temperature", "celsius", "fahrenheit", 0) == 32
    assert convert("temperature", "fahrenheit", "celsius", 32) == 0

def test_valid_distance_conversion():
    assert round(convert("distance", "kilometers", "miles", 1), 4) == 0.6214
    assert round(convert("distance", "miles", "kilometers", 1), 4) == 1.6093

def test_valid_currency_conversion():
    eur = convert("currency", "usd", "eur", 1)
    usd = convert("currency", "eur", "usd", eur)
    assert round(usd, 2) == pytest.approx(1.0, abs=0.05)

def test_invalid_domain():
    with pytest.raises(ValueError):
        convert("mass", "kg", "g", 1)

def test_invalid_units():
    with pytest.raises(ValueError):
        convert("temperature", "kelvin", "celsius", 100)
