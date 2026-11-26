import pytest
from Temperature import Temperature


def test_initialization():
    """
    Tests default unit, case-insensitive units, and read-only attributes
    """
    t_default = Temperature(25)
    assert t_default.value == 25.0
    assert t_default.unit == "C"

    t_lower_f = Temperature(32, "f")
    assert t_lower_f.value == 32.0
    assert t_lower_f.unit == "F"

    t_lower_k = Temperature(300, " k ")
    assert t_lower_k.value == 300.0
    assert t_lower_k.unit == "K"

    with pytest.raises(AttributeError):
        t_default.value = 10.0
    with pytest.raises(AttributeError):
        t_default.unit = "K"


def test_validation():
    """
    Tests invalid unit strings and temperatures below absolute zero
    """
    with pytest.raises(ValueError):
        Temperature(25, "X")
    with pytest.raises(ValueError):
        Temperature(25, "")

    with pytest.raises(ValueError):
        Temperature(-273.16, "C")
    with pytest.raises(ValueError):
        Temperature(-459.68, "F")
    with pytest.raises(ValueError):
        Temperature(-0.01, "K")


def test_conversions():
    """
    Tests conversion accuracy across reference points
    """
    abs_zero = Temperature(-273.15, "C")
    assert abs_zero.to_fahrenheit() == pytest.approx(-459.67)
    assert abs_zero.to_kelvin() == pytest.approx(0.0)

    cls_frht_crossover = Temperature(-40, "C")
    assert cls_frht_crossover.to_fahrenheit() == pytest.approx(-40.0)
    assert cls_frht_crossover.to_kelvin() == pytest.approx(233.15)

    frz_pt_wtr = Temperature(0, "C")
    assert frz_pt_wtr.to_fahrenheit() == pytest.approx(32.0)
    assert frz_pt_wtr.to_kelvin() == pytest.approx(273.15)

    hmn_bdy_tmp = Temperature(37, "C")
    assert hmn_bdy_tmp.to_fahrenheit() == pytest.approx(98.6)
    assert hmn_bdy_tmp.to_kelvin() == pytest.approx(310.15)

    blng_pt_wtr = Temperature(100, "C")
    assert blng_pt_wtr.to_fahrenheit() == pytest.approx(212.0)
    assert blng_pt_wtr.to_kelvin() == pytest.approx(373.15)

    with pytest.raises(ValueError):
        blng_pt_wtr.convert_to("X")


def test_round_trip_conversions():
    """
    Tests converting C -> F -> K -> C reproduces original Temperature
    """
    blng_pt_wtr = Temperature(100, "C")

    blng_pt_wtr_frht = blng_pt_wtr.convert_to("F")
    blng_pt_wtr_klvn = blng_pt_wtr_frht.convert_to("K")
    blng_pt_wtr_cls = blng_pt_wtr_klvn.convert_to("C")

    assert blng_pt_wtr_cls == blng_pt_wtr
    assert blng_pt_wtr_cls.unit == "C"
    assert blng_pt_wtr_cls.value == pytest.approx(blng_pt_wtr.value)


def test_cross_unit_comparisons():
    """
    Tests equality and ordering across mixed units
    """
    frz_c = Temperature(0, "C")
    frz_f = Temperature(32, "F")
    frz_k = Temperature(273.15, "K")
    blng_c = Temperature(100, "C")

    assert frz_c == frz_f
    assert frz_c == frz_k
    assert not (frz_c != frz_f)
    assert frz_c != blng_c

    assert frz_c < blng_c
    assert frz_f <= frz_k
    assert frz_c <= blng_c
    assert blng_c > frz_f
    assert frz_k >= frz_c
    assert blng_c >= frz_k

    assert (frz_c == 0) is False
    assert (frz_c != 0) is True


def test_formatting():
    """
    Tests outputs of str() and repr()
    """
    t = Temperature(25.0, "C")
    assert repr(t) == "Temperature(25.0, 'C')"
    assert str(t) == "25.00°C"