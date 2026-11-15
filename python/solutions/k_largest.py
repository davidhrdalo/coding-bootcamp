import heapq


def k_largest(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    heap: list[int] = []
    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)
        elif n > heap[0]:
            heapq.heappushpop(heap, n)
    return sorted(heap, reverse=True)
