import pytest
from unitflex.temperature import convert_temperature

def test_celsius_to_fahrenheit():
    assert convert_temperature("celsius", "fahrenheit", 100) == 212
    assert convert_temperature("celsius", "fahrenheit", -40) == -40

def test_fahrenheit_to_celsius():
    assert convert_temperature("fahrenheit", "celsius", 32) == 0
    assert convert_temperature("fahrenheit", "celsius", -40) == -40

def test_invalid_temperature_units():
    with pytest.raises(ValueError):
        convert_temperature("kelvin", "celsius", 300)
