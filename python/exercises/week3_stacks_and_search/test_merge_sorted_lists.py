from merge_sorted_lists import merge_sorted_lists


def test_interleaved():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_one_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    assert merge_sorted_lists([1, 2], []) == [1, 2]
    assert merge_sorted_lists([], []) == []


def test_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]


def test_different_lengths():
    assert merge_sorted_lists([1], [2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_inputs_are_not_modified():
    a, b = [1, 3], [2, 4]
    merge_sorted_lists(a, b)
    assert a == [1, 3]
    assert b == [2, 4]
