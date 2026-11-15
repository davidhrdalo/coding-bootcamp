"""Comparing floating-point numbers

Computers store decimals in binary, and most decimal fractions (like 0.1)
cannot be stored exactly. Try this in a Python shell:

    >>> 0.1 + 0.2
    0.30000000000000004
    >>> 0.1 + 0.2 == 0.3
    False

So you should never compare floats with ==. Instead check whether they are
CLOSE. Implement are_close(a, b, rel_tol, abs_tol) WITHOUT using math.isclose:

  return True when  abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

  are_close(0.1 + 0.2, 0.3)          -> True
  are_close(1.0, 1.1)                -> False
  are_close(0.0, 1e-12)              -> False  (relative tolerance means nothing near zero)
  are_close(0.0, 1e-12, abs_tol=1e-9) -> True

Concepts: IEEE 754 floating point, relative vs absolute tolerance.
Read theory/12-data-types.md.
"""


def are_close(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    raise NotImplementedError
