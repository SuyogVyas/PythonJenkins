import pytest
from calc import add,subtract

def test_add():
    assert add(8,11) == 19
    

def test_subtract():
    assert subtract(4,2) == 2
    