import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("2/4") == 50
    assert convert("99/100") == 99

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
