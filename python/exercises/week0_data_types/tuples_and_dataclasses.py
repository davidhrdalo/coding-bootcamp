"""Tuples and dataclasses

A tuple is an immutable sequence. It can be used as a dictionary key and is the
natural way to return several values. A dataclass is a class whose boilerplate
(__init__, __repr__, __eq__) is generated for you.

1. min_max(nums): return (smallest, largest) as a tuple, in ONE pass or using min()
   and max(). Raise ValueError if nums is empty.
     min_max([3, 1, 4, 1, 5]) -> (1, 5)

2. Point is a dataclass with float fields x and y. It is currently mutable. Change
   it so that a Point is IMMUTABLE and therefore hashable (so a Point can be a dict
   key), then add the method manhattan(other) that returns
   abs(x1 - x2) + abs(y1 - y2).
   (Hint: @dataclass(frozen=True).)

Concepts: tuples, immutability, hashing, dataclasses, unpacking
(low, high = min_max(nums)).
"""


from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def manhattan(self, other: "Point") -> float:
        raise NotImplementedError


def min_max(nums: list[int]) -> tuple[int, int]:
    raise NotImplementedError
