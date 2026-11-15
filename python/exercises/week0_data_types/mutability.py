"""Mutability traps

Lists, dicts and sets are MUTABLE (they change in place). Numbers, strings and
tuples are IMMUTABLE. Two classic bugs come from mixing that up.

1. The mutable default argument. This function looks fine but is broken:

       def add_tag(tag, tags=[]):
           tags.append(tag)
           return tags

   The default list is created ONCE, so every call without a second argument
   shares and keeps growing the same list. Write add_tag(tag, tags=None) so that it
   returns a NEW list containing the given tags (if any) followed by tag, and never
   modifies the list that was passed in.
     add_tag("a") -> ["a"]  and then  add_tag("b") -> ["b"]
     add_tag("y", ["x"]) -> ["x", "y"]   (the original ["x"] is unchanged)

2. The shallow copy. m2 = m[:] (or list(m)) copies the outer list but the inner
   rows are still the SAME objects. Write copy_matrix(matrix) that returns a list of
   lists where changing a number in the copy never changes the original.

Concepts: mutable vs immutable, aliasing, shallow vs deep copy, default arguments.
Tip: use Python Tutor (pythontutor.com) to see which names point at the same object.
"""


def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    raise NotImplementedError


def copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError
