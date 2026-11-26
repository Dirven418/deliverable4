from fractions import Fraction
import pytest


test1 = Fraction(1, 2)
test2 = Fraction(2, 4)
test3 = Fraction(1, 3)
test4 = Fraction(2, 1)

# test ValueError for invalid fractions
def test_fraction():
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(0.5, 2)

# test equality
def test__eq__():
    assert test1 == test2
    assert not test1 == test3
    
def test__ne__():
    assert test1 != test3
    assert not test1 != test2

def test__lt__():
    assert test3 < test1
    assert not test1 < test2

def test__le__():
    assert test1 <= test2
    assert test3 <= test1
    assert not test4 <= test1

def test__gt__():
    assert test1 > test3
    assert not test1 > test4

def test__ge__():
    assert test1 >= test2
    assert test1 >= test3
    assert not test1 >= test4

def test__repr__():
    assert repr(test1) == "<Fraction(1, 2)>"

def test__str__():
    assert str(test1) == "Fraction: 1 / 2"

def test__mul__():
    assert test1 * test2 == Fraction(2, 8)

def test__call__():
    assert test1() == pytest.approx(0.5)
    assert test3() == pytest.approx(0.333333, abs=1e-06)
