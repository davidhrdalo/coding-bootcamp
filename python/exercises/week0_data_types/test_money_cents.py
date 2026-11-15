import pytest

from money_cents import format_cents, to_cents


def test_whole_and_decimal_amounts():
    assert to_cents("5") == 500
    assert to_cents("5.5") == 550
    assert to_cents("19.99") == 1999
    assert to_cents("0.05") == 5
    assert to_cents("1000.00") == 100000


def test_the_classic_float_trap_is_avoided():
    assert to_cents("0.1") + to_cents("0.2") == to_cents("0.3")
    assert to_cents("1.15") == 115  # float("1.15") * 100 is 114.99999999999999


def test_result_is_an_int():
    assert type(to_cents("1.00")) is int


@pytest.mark.parametrize("bad", ["", "abc", "1.234", "-3", "1.2.3", ".5"])
def test_invalid_amounts_raise_value_error(bad):
    with pytest.raises(ValueError):
        to_cents(bad)


def test_format_cents():
    assert format_cents(0) == "$0.00"
    assert format_cents(5) == "$0.05"
    assert format_cents(1999) == "$19.99"
    assert format_cents(100000) == "$1000.00"


def test_round_trip():
    for text in ["0.01", "12.34", "99.99", "100.00"]:
        assert format_cents(to_cents(text)) == "$" + text
