"""Replace recursion with your own stack

Every function call uses the CALL STACK. Recursion that goes too deep
overflows it: in Python that raises RecursionError (the limit is about 1000
frames by default). You can avoid the problem by keeping your OWN stack in a
list instead. Read theory/02-stack-and-heap.md first.

Implement flatten(nested): given a list that may contain other lists nested to
any depth, return a flat list of all the non-list items in left-to-right order.

  flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
  flatten([]) -> []

Rule: do NOT write a recursive function. One test builds a list nested 5,000
levels deep, which a recursive solution cannot handle.

Hint: keep a stack of iterators. Look at the top iterator; if its next item is a
list, push an iterator for it, otherwise record the item; when an iterator is
exhausted, pop it.
"""


def flatten(nested: list) -> list:
    raise NotImplementedError
