from explicit_stack import flatten


def test_flat_list_is_unchanged():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_empty():
    assert flatten([]) == []
    assert flatten([[], [[]]]) == []


def test_nested_example():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]


def test_order_is_left_to_right():
    assert flatten([[1, 2], [3, [4, [5]]], 6, [[7]]]) == [1, 2, 3, 4, 5, 6, 7]


def test_strings_are_items_not_lists():
    assert flatten(["a", ["b", ["c"]]]) == ["a", "b", "c"]


def test_very_deep_nesting_does_not_overflow_the_stack():
    nested = [0]
    for i in range(1, 5000):
        nested = [i, nested]
    assert flatten(nested) == list(range(4999, -1, -1))
