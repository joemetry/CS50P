import pytest
from working import convert

def test_valid_times():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('1:00 PM to 11:00 PM') == '13:00 to 23:00'
    assert convert('12:15 PM to 12:45 AM') == '12:15 to 00:45'

def test_invalid_times():
    with pytest.raises(ValueError):
        convert('12:60 AM to 12:00 PM')
    with pytest.raises(ValueError):
        convert('13:00 PM to 1:00 PM')
    with pytest.raises(ValueError):
        convert('9 AM to 5 AM')
    with pytest.raises(ValueError):
        convert('9:00 to 5:00 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')

def test_invalid_format():
    with pytest.raises(ValueError):
        convert('9AM to 5PM')
    with pytest.raises(ValueError):
        convert('9:00AM to 5:00PM')
    with pytest.raises(ValueError):
        convert('09:00 to 17:00')
    with pytest.raises(ValueError):
        convert('nine AM to five PM')
