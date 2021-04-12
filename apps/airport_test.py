from doubles import allow
import pytest
from airport import Airport
from weather import Weather

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
    weather = Weather()
    airport.land("plane")
    allow(weather).weather_check.and_return('sunny')
    assert airport.hangar == ["plane"]

def test_airport_take_off():
    airport = Airport()
    weather = Weather()
    allow(weather).weather_check.and_return('sunny')
    airport.land("plane")
    airport.take_off("plane")
    assert airport.hangar == []

def test_airport_capacity():
    airport = Airport()
    weather = Weather()
    allow(weather).weather_check.and_return('sunny')
    airport.land("plane")
    airport.land("plane")
    airport.land("plane")
    assert airport.land("plane") == "Hangar Capacity Reached!"

def test_set_capacity():
    airport = Airport(1)
    airport.land("plane")
    assert airport.land("plane") == "Hangar Capacity Reached!"

def test_weather_take_off():
    airport = Airport()
    airport.land("plane")
    allow(airport).weather_check.and_return('stormy')
    assert airport.take_off("plane") == "Weather Troubles! No take offs permitted!"

def test_weather_land():
    airport = Airport()
    allow(airport.weather).and_return('stormy')
    assert airport.land("plane") == "Weather Troubles! No landings permitted!"