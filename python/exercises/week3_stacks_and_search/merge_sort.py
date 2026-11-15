"""Merge sort

Implement merge sort: split the list in half, sort each half (recursively),
then merge the two sorted halves (you wrote the merge step in merge_sorted_lists).
Return a NEW sorted list and do not modify the input. Do not use sorted() or
list.sort().

  merge_sort([5, 2, 9, 1]) -> [1, 2, 5, 9]

Concepts: divide and conquer, recursion, O(n log n) time, O(n) extra space, stable
sorting (equal items keep their original order).
Be able to explain why it is O(n log n): the list is halved log n times and each
level does O(n) work to merge.
"""


def merge_sort(nums: list[int]) -> list[int]:
    raise NotImplementedError
