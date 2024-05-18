import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, world!") == 0

def test_value_starts_with_h():
    assert value("hi") == 20
    assert value("Hi there!") == 20

def test_value_other():
    assert value("goodbye") == 100
    assert value("Good morning!") == 100

def test_value_case_insensitive():
    assert value("HELLO") == 0
    assert value("hELLO") == 0
    assert value("H") == 20
    assert value("Greeting") == 100
