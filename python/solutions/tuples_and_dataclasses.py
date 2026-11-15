from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def manhattan(self, other: "Point") -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)


def min_max(nums: list[int]) -> tuple[int, int]:
    if not nums:
        raise ValueError("nums must not be empty")
    return (min(nums), max(nums))
