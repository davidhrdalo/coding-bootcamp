"""Build a Stack class

Implement a Stack class (last in, first out) WITHOUT inheriting from list.
You may use a list internally.

Methods:
  push(item)     add item to the top
  pop()          remove and return the top item; raise IndexError if empty
  peek()         return the top item without removing it; raise IndexError if empty
  is_empty()     True if there are no items
  len(stack)     number of items (implement __len__)

Concepts: classes, encapsulation, exceptions, LIFO.
"""


class Stack:
    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, item) -> None:
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
