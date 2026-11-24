

class Temperature:

    def __init__(self, value, unit):

        unit_stripped = unit.strip().upper()

        if unit_stripped not in ("C", "F", "K"):
            raise ValueError("Unvalid unit")

        self._value = float(value)
        self._unit = unit_stripped

        if self.to_kelvin() < -1e-9:
            raise ValueError("Temperaturen må være over absolutt 0")


    def to_celsius(self):
        if self._unit == "C":
            return self._value
        elif self._unit == "K":
            return self._value - 273.15
        elif self._unit == "F":
            return (self._value - 32) * (5/9)

    def to_fahrenheit(self):
        if self._unit == "F":
            return self._value
        return self.to_celsius() * (9/5) + 32

    def to_kelvin(self):
        if self._unit == "K":
            return self._value
        return self.to_celsius() + 273.15

    def convert_to(self, target_unit: str, target_value):

        self.target_unit = target_unit
        self.target_value = target_value


    def __repr__(self):
        return f"""
        Temperature({self._value},{self._unit}) to Temperature({self.target_value} new unit={self._target_unit})
        """

    def __str__(self):
        return f"""
        {self._value:.2f} °{self._unit} to {self.target_value:.2f} °{self._value}
        """

    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) < 1e-9

    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return not (self == other)

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() - other.to_kelvin()) <= 1e-9

    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self < other) or (self == other)

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return (other.to_kelvin() - self.to_kelvin()) <= 1e-9

    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self > other) or (self == other)