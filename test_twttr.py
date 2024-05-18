import pytest
from twttr import shorten

def test_shorten_empty():
    assert shorten("") == ""

def test_shorten_no_vowels():
    assert shorten("bcdfg") == "bcdfg"

def test_shorten_all_vowels():
    assert shorten("aeiou") == ""

def test_shorten_mixed_case():
    assert shorten("aEiOu") == ""

def test_shorten_mixed_characters():
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_shorten_numbers():
    assert shorten("12345") == "12345"
