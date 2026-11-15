from binary_search import binary_search


def test_found():
    nums = [1, 3, 5, 7, 9]
    for i, value in enumerate(nums):
        assert binary_search(nums, value) == i


def test_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1


def test_empty_and_single():
    assert binary_search([], 1) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 4) == -1


def test_duplicates_returns_a_valid_index():
    nums = [1, 2, 2, 2, 3]
    assert nums[binary_search(nums, 2)] == 2


def test_large_list():
    nums = list(range(0, 2_000_000, 2))
    assert binary_search(nums, 1_999_998) == 999_999
    assert binary_search(nums, 1_999_999) == -1
