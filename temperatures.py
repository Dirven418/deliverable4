class Temperature:
    """"""

    def __init__(self, value: float, unit: str) -> None:
        """Initialize the temperature object containing the value and unit"""
        self._value = value   # Read only attribute
        self._unit = str.upper(unit)   # Read only attribute

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

        if target_unit not in ["C", "F", "K"]:
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

