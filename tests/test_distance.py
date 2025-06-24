import pytest
from unitflex.distance import convert_distance

def test_kilometers_to_miles():
    assert round(convert_distance("kilometers", "miles", 5), 4) == 3.1069

def test_miles_to_kilometers():
    assert round(convert_distance("miles", "kilometers", 3.1), 4) == 4.9888

def test_invalid_distance_units():
    with pytest.raises(ValueError):
        convert_distance("meters", "miles", 1000)
