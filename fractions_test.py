from Fractions import Fraction
import pytest


fraction1 = Fraction(1, 2)
fraction2 = Fraction(2, 4)
fraction3 = Fraction(1, 3)
fraction4 = Fraction(2, 1)

# test ValueError for invalid fractions
def test_fraction():
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(0.5, 2)

# test equality
def test__eq__():
    assert fraction1 == fraction2
    assert not fraction1 == fraction3
    
def test__ne__():
    assert fraction1 != fraction3
    assert not fraction1 != fraction2

def test__lt__():
    assert fraction3 < fraction1
    assert not fraction1 < fraction2

def test__le__():
    assert fraction1 <= fraction2
    assert fraction3 <= fraction1
    assert not fraction4 <= fraction1

def test__gt__():
    assert fraction1 > fraction3
    assert not fraction1 > fraction4

def test__ge__():
    assert fraction1 >= fraction2
    assert fraction1 >= fraction3
    assert not fraction1 >= fraction4

def test__repr__():
    assert repr(fraction1) == "<Fraction(1, 2)>"

def test__str__():
    assert str(fraction1) == "Fraction: 1 / 2"

def test__mul__():
    assert fraction1 * fraction2 == Fraction(2, 8)

def test__call__():
    assert fraction1() == pytest.approx(0.5)
    assert fraction3() == pytest.approx(0.333333, abs=1e-06)
