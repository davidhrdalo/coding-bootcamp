import pytest

from fibonacci import fibonacci


def test_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def test_small_values():
    assert [fibonacci(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_ten():
    assert fibonacci(10) == 55


def test_negative_raises_value_error():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_large_value_needs_an_efficient_solution():
    assert fibonacci(50) == 12586269025
