import pytest
from temperatures import Temperature


def test_initialization():
    """Test the initialization in Temperature class"""

    # Test default unit
    t1 = Temperature(20)
    t2 = Temperature(20, "F")

    assert t1._unit == "C"
    assert t2._unit == "F"

    # Test case-insensitive units
    t3 = Temperature(20, "f")
    assert t3._unit == "F"

    # Test read-only behavior
    with pytest.raises(AttributeError):
        t2.value = 70

    with pytest.raises(AttributeError):
        t2.unit = "K"


@pytest.mark.parametrize("attribute",
                         ["value",
                         "unit"
                         ])

    

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

def test_conversions():

def test_round_trip_conversion():

def test_cross_unit_comparisons():

def test_formatting():
