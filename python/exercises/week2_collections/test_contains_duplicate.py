from contains_duplicate import contains_duplicate


def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_no_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_empty_and_single():
    assert contains_duplicate([]) is False
    assert contains_duplicate([7]) is False


def test_large_input():
    assert contains_duplicate(list(range(100000))) is False
    assert contains_duplicate(list(range(100000)) + [5]) is True
