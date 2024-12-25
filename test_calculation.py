import pytest
from calc import add,subtract

@pytest.mark.addition
def test_add():
    assert add(8,11) == 19
    assert add(8,4) == 2

    

def test_subtract():
    assert subtract(4,2) == 2
    assert subtract(3,4) == 11
    assert subtract(44,44) == 0