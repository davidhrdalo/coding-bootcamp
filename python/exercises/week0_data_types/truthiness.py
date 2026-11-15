"""Truthiness: what counts as true or false

In Python every value is either truthy or falsy when used in an if. The FALSY
values are: None, False, zero (0, 0.0), and empty containers or strings
("", [], {}, set(), ()). Everything else is truthy, including "0", "False" and [0].

first_truthy(*values): return the first truthy value, or None if there is none.
  first_truthy(0, "", None, "x", 5) -> "x"

falsy_kind(value): describe a value as one of these strings:
  "none"    for None
  "false"   for the boolean False
  "zero"    for the numbers 0 and 0.0 (but NOT for False)
  "empty"   for an empty string, list, dict, set or tuple
  "truthy"  for anything else
Careful: False == 0 in Python, and bool is a subclass of int, so the order of
your checks matters.

Concepts: truthiness, None, is vs ==, isinstance. (Note JavaScript's falsy values
are different: 0, "", null, undefined, NaN, false. An empty array is truthy there.)
"""


def first_truthy(*values):
    raise NotImplementedError


def falsy_kind(value) -> str:
    raise NotImplementedError
