import random

from merge_sort import merge_sort


def test_basic():
    assert merge_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_and_single():
    assert merge_sort([]) == []
    assert merge_sort([3]) == [3]


def test_already_sorted_and_reversed():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates_and_negatives():
    assert merge_sort([3, -1, 3, 0, -1]) == [-1, -1, 0, 3, 3]


def test_input_is_not_modified_and_a_new_list_is_returned():
    original = [3, 1, 2]
    result = merge_sort(original)
    assert original == [3, 1, 2]
    assert result is not original


def test_matches_builtin_sorted_on_random_data():
    rng = random.Random(1234)
    for size in (2, 10, 101, 1000):
        data = [rng.randint(-1000, 1000) for _ in range(size)]
        assert merge_sort(data) == sorted(data)


def test_large_input_is_fast_enough():
    rng = random.Random(99)
    data = [rng.random() for _ in range(100_000)]
    assert merge_sort(data) == sorted(data)
