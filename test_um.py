import pytest
from um import count

def test_count_um():
    assert count('hello, um, world') == 1
    assert count('Um, I think um is, um, used too often.') == 3
    assert count('Yummy food') == 0
    assert count('Some words: rum, drum, aluminum.') == 0
    assert count('um um um') == 3
    assert count('UM') == 1
    assert count('uM uM') == 2

def test_empty_string():
    assert count('') == 0

def test_no_um():
    assert count('This sentence does not contain the word.') == 0
