"""Fibonacci

Return the nth Fibonacci number, where F(0) = 0, F(1) = 1 and
F(n) = F(n-1) + F(n-2). Raise ValueError if n is negative.

Examples:
  fibonacci(10) -> 55
  fibonacci(50) -> 12586269025

Concepts: loops, state, time complexity.
Warning: the obvious recursive version recomputes the same values again and again
(exponential time). The last test uses n = 50, so a naive recursive solution will
effectively never finish. If it hangs, press Ctrl+C and think about how to avoid
repeated work (a loop with two variables, or memoisation with functools.cache).
"""


def fibonacci(n: int) -> int:
    raise NotImplementedError
