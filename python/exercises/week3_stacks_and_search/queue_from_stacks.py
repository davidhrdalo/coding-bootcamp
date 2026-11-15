"""A queue built from two stacks

A queue is first-in, first-out (FIFO). A stack is last-in, first-out (LIFO).
A famous interview question: build a queue using only stacks.

Implement QueueFromStacks with:
  enqueue(item)   add to the back
  dequeue()       remove and return the front item; raise IndexError if empty
  peek()          return the front item without removing it; raise IndexError if empty
  is_empty()      True if there are no items
  len(queue)      number of items (implement __len__)

Rules: keep two plain lists and use them ONLY as stacks (append and pop from the
END). Do not use pop(0) or collections.deque.

Idea: push new items onto an "in" stack. To dequeue, if the "out" stack is empty,
move everything from "in" to "out" (this reverses the order), then pop from "out".
Each item moves at most once, so every operation is O(1) amortised.

Concepts: LIFO vs FIFO, amortised analysis.
"""


class QueueFromStacks:
    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, item) -> None:
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
