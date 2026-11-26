import pytest
from temperatures import Temperature

# Making temperatures that can be used in the tests
t1 = Temperature(20)
t2 = Temperature(20, "F")
t3 = Temperature(20, "f")
t4 = Temperature(100, "C")
t5 = Temperature(212, "F")
t6 = Temperature(310.15, "K")
t7 = Temperature(0, "K")


def test_initialization():
    """Test the initialization in Temperature class"""

    # Test default unit
    assert t1._unit == "C"
    assert t2._unit == "F"

    # Test case-insensitive units
    assert t3._unit == "F"

    # Test read-only behavior
    with pytest.raises(AttributeError):
        t2.value = 70

    with pytest.raises(AttributeError):
        t2.unit = "K"


def test_validation():
    """Test the validation of values and units in Temperature class"""

    # Test invalid unit strings
    with pytest.raises(ValueError):
        Temperature(20, "U")

    # Test temperatures below absolute zero
    with pytest.raises(ValueError):
        Temperature(-300, "C")

    with pytest.raises(ValueError):
        Temperature(-600, "F")

    with pytest.raises(ValueError):
        Temperature(-20, "K")


# Making reference points to test
@pytest.mark.parametrize("C, F, K",
                         [[-273.15, -459.67, 0],
                          [-40, -40, 233.15],
                          [0, 32, 273.15],
                          [37, 98.6, 310.15],
                          [100, 212, 373.15]
                          ])
def test_conversions(C, F, K):
    """Test conversion accuracy across reference points"""
    temp = Temperature(C, "C")

    assert temp.to_fahrenheit() == pytest.approx(F, 1e-9) and temp.to_kelvin() == pytest.approx(K, 1e-9)


def test_round_trip_conversion():
    """Testing if converting several times reproduces the original temperature"""
    convert_1 = Temperature(t4.to_fahrenheit(), "F")
    convert_2 = Temperature(convert_1.to_kelvin(), "K")

    assert convert_2.to_celsius() == pytest.approx(t4._value, 1e-9)


def test_cross_unit_comparisons():
    assert t4 == t5
    assert t2 != t4
    assert t7 < t4
    assert t4 <= t5
    assert t5 > t7
    assert t5 >= t6


def test_formatting():
    assert str(t2) == "The temperature is 20.00 °F"
    assert repr(t2) == "Temperature(20.0, 'F')"
