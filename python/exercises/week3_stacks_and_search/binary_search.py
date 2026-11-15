"""Binary search

nums is sorted in ascending order. Return the index of target, or -1 if it
is not present. If the value appears more than once, any matching index is fine.

Examples:
  binary_search([1, 3, 5, 7, 9], 7) -> 3
  binary_search([1, 3, 5, 7, 9], 4) -> -1

Concepts: divide and conquer, O(log n), off-by-one errors.
Write it with a loop (while low <= high), not with list slicing.
"""


def binary_search(nums: list[int], target: int) -> int:
    raise NotImplementedError
