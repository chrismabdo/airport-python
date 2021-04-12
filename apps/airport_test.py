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

def test_airport_take_off():
    airport = Airport()
    airport.land("plane")
    airport.take_off("plane")
    assert airport.hangar == []

def test_airport_capacity():
    airport = Airport()
    airport.land("plane")
    airport.land("plane")
    airport.land("plane")
    assert airport.land("plane") == "Hangar Capacity Reached!"

def test_set_capacity():
    airport = Airport(1)
    airport.land("plane")
    assert airport.land("plane") == "Hangar Capacity Reached!"

def test_weather():
    airport = Airport()
    airport.land("plane")
    assert airport.take_off("plane") == "Weather Troubles! No take offs permitted!"
