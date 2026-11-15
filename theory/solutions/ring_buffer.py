class RingBuffer:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._data = [None] * capacity
        self._capacity = capacity
        self._start = 0
        self._size = 0

    def push(self, item) -> None:
        if self._size == self._capacity:
            # Full: overwrite the oldest item and move the start forward.
            self._data[self._start] = item
            self._start = (self._start + 1) % self._capacity
        else:
            end = (self._start + self._size) % self._capacity
            self._data[end] = item
            self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty RingBuffer")
        item = self._data[self._start]
        self._data[self._start] = None
        self._start = (self._start + 1) % self._capacity
        self._size -= 1
        return item

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def to_list(self) -> list:
        return [self._data[(self._start + i) % self._capacity] for i in range(self._size)]

    def __len__(self) -> int:
        return self._size
