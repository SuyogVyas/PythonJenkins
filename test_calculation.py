import pytest
from calc import add,subtract

def test_add():
    assert add(3,4) == 7
    assert add(8,11) == 19
    


def test_subtract():
    assert subtract(4,2) == 2
    assert subtract(3,4) == 4
    assert subtract(44,44) == 2