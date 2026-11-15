"""Converting between types safely

Data from the outside world (files, forms, APIs) usually arrives as text, and
converting it can fail. Implement:

parse_int(text, default=0): convert text to an int. If it cannot be converted
(not a number, empty, a decimal like "4.2", or not even a string such as None),
return default instead of raising.
  parse_int("42") -> 42       parse_int(" 42 ") -> 42      parse_int("-7") -> -7
  parse_int("4.2") -> 0       parse_int("abc", default=-1) -> -1

to_bool(text): convert text to a real boolean. Case-insensitive, ignoring
surrounding spaces:
  "true", "yes", "1", "on"   -> True
  "false", "no", "0", "off"  -> False
  anything else raises ValueError
Why not just bool(text)? Because bool("False") is True: any non-empty string is truthy.

Concepts: explicit conversion, exceptions (try/except), validating input.
"""


def parse_int(text, default: int = 0) -> int:
    raise NotImplementedError


def to_bool(text: str) -> bool:
    raise NotImplementedError
