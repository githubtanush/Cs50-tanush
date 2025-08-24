from calculator import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

#pytest like library automatically running all these tests 
#for me 
#download pytest as pip3 command 
#and run in terminal pytest test_calculator2.py
