

class fraction:
    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if(
            not isinstance(numerator, int) 
            or isinstance(numerator, bool)
            or not isinstance(denominator, int)
            or isinstance(denominator, bool)
        ):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer.")

# store the values of numerator and denominator
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

# the six special methods for comparison

    # equal 
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    # not equal
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator != self.denominator * other.numerator

    # less than
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator

    # less than or equal to
    def __le__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator <= self.denominator * other.numerator

    # greater than
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator

    # greater than or equal to
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, fraction):
            return NotImplemented
        return self.numerator * other.denominator >= self.denominator * other.numerator


#four other special methods

    # string representation of the fraction for debugging
    def __repr__(self) -> str:
        return f"fraction {self.numerator}/{self.denominator}"

    # string representation of the fraction
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    # addition of two fractions
    def __add__(self, other: object) -> "fraction":
        if not isinstance(other, fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    # multiplication of two fractions
    def __mul__(self, other: object) -> "fraction":
        if not isinstance(other, fraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)
