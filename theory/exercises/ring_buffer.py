"""Ring buffer (circular buffer)

A ring buffer is a fixed-size queue stored in one array that wraps around.
It is used for audio, network packets, logs and keyboard input: places where data
arrives continuously and you only want the most recent items.
Read theory/04-buffers-and-streams.md first.

Implement RingBuffer(capacity):
  push(item)   add item at the end. If the buffer is already full, overwrite the
               OLDEST item (the buffer never grows).
  pop()        remove and return the oldest item; raise IndexError if empty
  len(buf)     number of items currently stored (implement __len__)
  is_empty()   True if len is 0
  is_full()    True if len equals capacity
  to_list()    items from oldest to newest, without removing them

Raise ValueError if capacity is less than 1.

Use a fixed-size list plus a start index and a size, and wrap indexes with the
modulo operator (%). Do not use collections.deque and do not grow the list.
"""


class RingBuffer:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def push(self, item) -> None:
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
