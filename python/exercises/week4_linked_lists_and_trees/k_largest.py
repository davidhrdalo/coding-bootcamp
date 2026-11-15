"""The k largest values (heap)

Return the k largest values of nums, in DESCENDING order. If k is larger than
the list, return everything (still sorted descending). If k <= 0, return [].

  k_largest([5, 1, 9, 3, 7], 2) -> [9, 7]

A heap (priority queue) makes this O(n log k), much better than sorting everything
(O(n log n)) when k is small. Python's heapq module is a MIN-heap: the smallest
item is always at the front. Trick: keep a min-heap of size k containing the k
largest values seen so far. For each new number, if the heap is not full push it;
otherwise, if the number is larger than the smallest item in the heap
(heap[0]), replace the smallest (heapq.heappushpop).

Implement it by hand with heappush / heappushpop first. heapq.nlargest does the same
job in one call, but using it straight away would skip the lesson.

Concepts: heaps and priority queues, min-heap vs max-heap, choosing the right data structure.
"""


def k_largest(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError
