import random

from k_largest import k_largest


def test_basic():
    assert k_largest([5, 1, 9, 3, 7], 2) == [9, 7]


def test_k_of_one():
    assert k_largest([5, 1, 9, 3, 7], 1) == [9]


def test_duplicates_are_counted():
    assert k_largest([4, 4, 4, 1], 2) == [4, 4]


def test_k_larger_than_the_list_returns_everything_sorted_descending():
    assert k_largest([2, 3, 1], 10) == [3, 2, 1]


def test_zero_negative_k_and_empty_input():
    assert k_largest([1, 2, 3], 0) == []
    assert k_largest([1, 2, 3], -1) == []
    assert k_largest([], 3) == []


def test_negative_numbers():
    assert k_largest([-5, -1, -9, -3], 2) == [-1, -3]


def test_input_is_not_modified():
    data = [3, 1, 2]
    k_largest(data, 2)
    assert data == [3, 1, 2]


def test_large_input():
    rng = random.Random(7)
    data = [rng.randint(0, 10_000_000) for _ in range(200_000)]
    assert k_largest(data, 10) == sorted(data, reverse=True)[:10]
