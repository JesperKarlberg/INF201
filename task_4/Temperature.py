

class Temperature:

    def __init__(self, value, unit="C"):
        """
        Splitting the value to sort the unit
        If the unit is not defined we raise a ValueError
        self._value = Input number
        self._unit = Input unit
        Defines the floor for absolute zero
        """

        if not isinstance(unit, str):
            raise ValueError("Unvalid unit")

        unit_stripped = unit.strip().upper()

        if unit_stripped not in ("C", "F", "K"):
            raise ValueError("Unvalid unit")

        self._value = float(value)
        self._unit = unit_stripped

        if self.to_kelvin() < -1e-9:
            raise ValueError("The temperature must be above absolute zero")

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit
    

    def to_celsius(self):
        """"
        Checks if the value is in Celsius,
        if not then we translate it into Celsius
        """
        if self._unit == "C":
            return self._value
        elif self._unit == "K":
            return self._value - 273.15
        elif self._unit == "F":
            return (self._value - 32) * (5/9)

    def to_fahrenheit(self):
        """"
        Checks if the value is in Fahrenheit
        if not then we send it through the Celsius function
        then translate the value to Fahrenheit
        """
        if self._unit == "F":
            return self._value
        return self.to_celsius() * (9/5) + 32

    def to_kelvin(self):
        """"
        Checks if the value is in Kelvin
        if not then we send it through the Celsius function
        then translate the value to Kelvin
        """
        if self._unit == "K":
            return self._value
        return self.to_celsius() + 273.15

    def convert_to(self, target_unit: str):
        """"
        Creates a new instance of the converted value
        """

        if not isinstance(target_unit, str):
            raise ValueError("Unvalid unit")

        unit_stripped = target_unit.strip().upper()

        if unit_stripped == "C":
            return Temperature(self.to_celsius(), "C")
        elif unit_stripped == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif unit_stripped == "K":
            return Temperature(self.to_kelvin(), "K")
        else:
            raise ValueError("Unvalid unit")   
        

    def __repr__(self):
        """"
        Returns an unambigous representation
        """

        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self):
        """"
        Returns a human-readable string
        """
        return f"{self._value:.2f}°{self._unit}"

    def __eq__(self, other):
        """
        is equal to
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) < 1e-9

    def __ne__(self, other):
        """
        is not equal to
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other)

    def __lt__(self, other):
        """
        is less than
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() - other.to_kelvin()) < -1e-9

    def __le__(self, other):
        """
        is less than or equal to
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self < other) or (self == other)

    def __gt__(self, other):
        """
        is greater than
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return (other.to_kelvin() - self.to_kelvin()) < -1e-9

    def __ge__(self, other):
        """
        is greater than or equal to
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self > other) or (self == other)