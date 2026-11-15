import pytest

from factorial import factorial


def test_small_values():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_larger_value():
    assert factorial(10) == 3628800


def test_negative_raises_value_error():
    with pytest.raises(ValueError):
        factorial(-1)
