
class Fraction:
    """A fractions object containing a numerator and a positive denominator
    
    Args:
        Numerator: Numerator of the fraction
        Denominator: Denominator of the fraction
        
    Raises:
        AssertionError: Values are invalid"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialise the fraction object
        Args:
            numerator: represents the integer above the fraction line
            denominator: represents the integer below the fraction line

        Raises:
            AssertionError: Values are invalid
        """
        # check that inputs are valid
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer greater than 0.")

        if type(denominator) is not int or type(numerator) is not int:
            raise ValueError("numerator and denominator must be integers.")

        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other: Fraction | int) -> bool:
        """Evaluates if a Fraction is equal to another Fraction or value"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator == other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the fraction would be other over 1
        except:
            if self.numerator * 1 == other * self.denominator:
                return True
            else:
                return False


    def __ne__(self, other: Fraction | int) -> bool:
        """Evaluates if a Fraction is not equal to another Fraction or value"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator != other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the inverse fraction would be other over 1
        except:
            if self.numerator * 1 != other * self.denominator:
                return True
            else:
                return False

    def __lt__(self, other: Fraction | int) -> bool:
        """Checks if self is less than other"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator < other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the inverse fraction would be other over 1
        except:
            if self.numerator * 1 < other * self.denominator:
                return True
            else:
                return False

    def __le__(self, other: Fraction | int) -> bool:
        """Checks if self is less than or equal other"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator <= other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the inverse fraction would be other over 1
        except:
            if self.numerator * 1 <= other * self.denominator:
                return True
            else:
                return False


    def __gt__(self, other: Fraction | int) -> bool:
        """Checks if self is greater than other"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator > other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the inverse fraction would be other over 1
        except:
            if self.numerator * 1 > other * self.denominator:
                return True
            else:
                return False

    def __ge__(self, other: Fraction | int) -> bool:
        """Checks if self is greater than or equal other"""

        # try if other is a Fraction object
        try:
            # Multiplying by inverse fraction to avoid floating point errors
            if self.numerator * other.denominator >= other.numerator * self.denominator:
                return True
            else:
                return False

        # if other is a number the inverse fraction would be other over 1
        except:
            if self.numerator * 1 >= other * self.denominator:
                return True
            else:
                return False

    def __repr__(self) -> str:
        """representation of a Fraction object"""
        return f"<Fraction({self.numerator}, {self.denominator})>"

    def __str__(self) -> str:
        """String representation of a Fraction object"""
        return f"Fraction: {self.numerator} / {self.denominator}"

    def __mul__(self, other: Fraction | int) -> Fraction:
        """Determines how multiplaying two fraction objects works"""
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
            )

    def __call__(self) -> int | float:
        """returns a int or float for the fraction"""
        return self.numerator / self.denominator
