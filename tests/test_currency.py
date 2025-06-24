import pytest
from unitflex.currency import convert_currency

def test_usd_to_eur():
    eur = convert_currency("usd", "eur", 100)
    assert eur > 0

def test_eur_to_usd():
    usd = convert_currency("eur", "usd", 100)
    assert usd > 0

def test_invalid_currency_units():
    with pytest.raises(ValueError):
        convert_currency("usd", "gbp", 100)
