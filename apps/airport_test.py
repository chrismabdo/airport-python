import pytest
from airport import Airport
NUMBER_1 = 3
NUMBER_2 = 2

def test_add():
    value = NUMBER_1 + NUMBER_2
    assert value == 5

def test_airport_has_hangar():
    airport = Airport()
    assert airport.hangar == []

def test_airport_land():
    airport = Airport()
    airport.land("plane")
    assert airport.hangar == ["plane"]