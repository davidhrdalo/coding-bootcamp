from dataclasses import FrozenInstanceError

import pytest

from tuples_and_dataclasses import Point, min_max


def test_min_max_returns_a_tuple():
    result = min_max([3, 1, 4, 1, 5])
    assert result == (1, 5)
    assert isinstance(result, tuple)


def test_min_max_single_and_negative_values():
    assert min_max([7]) == (7, 7)
    assert min_max([-5, -1, -9]) == (-9, -1)


def test_min_max_empty_raises():
    with pytest.raises(ValueError):
        min_max([])


def test_unpacking_the_result():
    low, high = min_max([10, 20, 30])
    assert (low, high) == (10, 30)


def test_points_with_equal_values_are_equal():
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(2, 1)


def test_point_is_immutable():
    p = Point(1, 2)
    with pytest.raises(FrozenInstanceError):
        p.x = 5


def test_point_can_be_a_dictionary_key():
    names = {Point(0, 0): "origin", Point(1, 1): "one-one"}
    assert names[Point(0, 0)] == "origin"
    assert len({Point(1, 2), Point(1, 2)}) == 1


def test_manhattan_distance():
    assert Point(0, 0).manhattan(Point(3, 4)) == 7
    assert Point(-1, -1).manhattan(Point(1, 1)) == 4
    assert Point(2, 2).manhattan(Point(2, 2)) == 0
