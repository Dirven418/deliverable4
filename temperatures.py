import math


class Temperature:
    """Represents a temperature in celsius, fahrenheit or kelvin with value and unit"""

    TOL = 1e-9   # Tolerance for floating-point value comparisons

    def __init__(self, value: float, unit: str) -> None:
        """Initialize the temperature object containing the value and unit"""
        self._value = float(value)   # Read only attribute
        self._unit = str.upper(unit)   # Read only attribute and unit is case-insensitive

        if self._unit not in ["C", "F", "K"]:
            raise ValueError('Unit must be either "C", "F", or "K"')

        if self._value < 0 and self._unit == "K":
            raise ValueError('The temperature can not be below absolute zero (0 K)')

        if self._value < 273.15 and self._unit == "C":
            raise ValueError('The temperature can not be below absolute zero (273.15 C)')

        if self._value < -459.67 and self._unit == "F":
            raise ValueError('The temperature can not be below absolute zero (-459.67 F)')

    def to_celsius(self) -> float:
        """Convert the temperatures in kelvin or fahrenheit to celsius"""
        if self._unit == "K":
            return self._value - 273.15

        elif self._unit == "F":
            return (self._value - 32) * 5 / 9

    def to_fahrenheit(self) -> float:
        """Convert the temperatures in celsius or kelvin to fahrenheit"""
        if self._unit == "C":
            return self._value * 9 / 5 + 32

        elif self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Convert the temperatures in celsius or fahrenheit to kelvin"""
        if self._unit == "C":
            return self._value + 273.15

        elif self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15

    def convert_to(self, target_unit: str) -> Temperature:
        """Returns a new Temperature instance converted to target_unit"""
        target_unit = str.upper(target_unit)   # Target unit is case-insensitive

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")

        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")

        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")

        else:
            raise ValueError('Unit must be either "C", "F", or "K"')

    def __repr__(self) -> str:
        """Representation of temperature object"""
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        """String representation of temperature object"""
        if self._unit == "C" or self._unit == "F":
            return f"The temperature is {self._value:.2f} °{self._unit}"

        else:
            return f"The temperature is {self._value:.2f} {self._unit}"

    def is_equal(self, other: Temperature) -> bool:
        """Convert the temperatures to celsius and check if they are approximately equal"""
        return math.isclose(
            self._value.to_celsius(),
            other._value.to_celsius(),
            rel_tol=0,
            abs_tol=self.TOL
            )

    def __eq__(self, other: Temperature) -> bool:
        """Check if two temperatures are equal"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.is_equal(other)

    def __ne__(self, other: Temperature) -> bool:
        """Check if two temperatures are not equal"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self.is_equal(other)

    def __lt__(self, other: Temperature) -> bool:
        """Check if the temperature is less than another temperature"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() < other.to_celsius() - self.TOL

    def __le__(self, other: Temperature) -> bool:
        """Check if the temperature is less than or equal another temperature"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() < other.to_celsius() or self.is_equal(other)

    def __gt__(self, other: Temperature) -> bool:
        """Check if the temperature is greater than another temperature"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() > other.to_celsius() + self.TOL

    def __ge__(self, other: Temperature) -> bool:
        """Check if the temperature is greater than or equal another temperature"""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() > other.to_celsius() or self.is_equal(other)
