import pytest
from plates import is_valid

def test_is_valid_length():
    assert is_valid("AB123")
    assert not is_valid("A123456")
    assert not is_valid("A")

def test_is_valid_start():
    assert is_valid("AB123")
    assert not is_valid("1AB123")
    assert not is_valid("AB")

def test_is_valid_alphanumeric():
    assert is_valid("AB123")
    assert not is_valid("AB123!")
    assert not is_valid("AB-123")

def test_is_valid_end():
    assert is_valid("AB123")
    assert not is_valid("AB123A")
    assert not is_valid("AB1234A")

def test_is_valid_zero():
    assert is_valid("AB123")
    assert not is_valid("AB0123")
    assert is_valid("AB100")
