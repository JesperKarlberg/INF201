import pytest
from fraction import fraction  # Change to: from task_2.fraction import fraction (if in a subfolder)


def test_fraction_init():
    # Valid initialization and property getters
    f1 = fraction(3, 4)
    assert f1.numerator == 3
    assert f1.denominator == 4

    # Default denominator = 1
    f2 = fraction(5)
    assert f2.numerator == 5
    assert f2.denominator == 1

    # Invalid types raise TypeError (including booleans)
    with pytest.raises(TypeError):
        fraction(1.5, 2)
    with pytest.raises(TypeError):
        fraction(True, 2)

    # Zero or negative denominator raises ValueError
    with pytest.raises(ValueError):
        fraction(1, 0)
    with pytest.raises(ValueError):
        fraction(1, -3)


def test_fraction_comparisons():
    f1 = fraction(1, 2)
    f2 = fraction(2, 4)
    f3 = fraction(3, 4)

    # Test all six comparison operators
    assert f1 == f2
    assert f1 != f3
    assert f1 < f3
    assert f1 <= f2
    assert f3 > f1
    assert f3 >= f2


def test_fraction_str_and_repr():
    f = fraction(3, 4)

    # Test human-readable (__str__) and developer (__repr__) representations
    assert str(f) == "3/4"
    assert repr(f) == "fraction 3/4"


def test_fraction_add_and_mul():
    f1 = fraction(1, 2)
    f2 = fraction(1, 3)

    # Test addition (__add__) and multiplication (__mul__)
    assert f1 + f2 == fraction(5, 6)
    assert f1 * f2 == fraction(1, 6)