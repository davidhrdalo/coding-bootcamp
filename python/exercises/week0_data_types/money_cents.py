"""Money without floats

Never store money in floats (see float_compare). The usual fix is to store
whole CENTS as an integer. Implement two functions:

to_cents(amount): convert a string like "19.99" into the integer 1999.
  - digits before the point are required: "5" -> 500, "5.5" -> 550, "0.05" -> 5
  - at most two digits after the point
  - anything else ("", "abc", "1.234", "-3") raises ValueError
  - do NOT use float() anywhere (that would bring the rounding error back)

format_cents(cents): convert a non-negative integer of cents into text such as
"$19.99" (always two decimal places, no thousands separators).
  format_cents(5) -> "$0.05"
  format_cents(100000) -> "$1000.00"

Concepts: integers vs floats, string parsing, validation.
"""


def to_cents(amount: str) -> int:
    raise NotImplementedError


def format_cents(cents: int) -> str:
    raise NotImplementedError
