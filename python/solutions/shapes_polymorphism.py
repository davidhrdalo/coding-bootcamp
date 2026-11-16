from abc import ABC, abstractmethod
import math


def _positive(value: float) -> float:
    if value <= 0:
        raise ValueError("sizes must be greater than zero")
    return value


class Shape(ABC):
    name = "shape"

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    name = "circle"

    def __init__(self, radius: float) -> None:
        self.radius = _positive(radius)

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    name = "rectangle"

    def __init__(self, width: float, height: float) -> None:
        self.width = _positive(width)
        self.height = _positive(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    name = "square"

    def __init__(self, side: float) -> None:
        super().__init__(side, side)


def largest(shapes: list) -> Shape:
    if not shapes:
        raise ValueError("no shapes")
    best = shapes[0]
    for shape in shapes[1:]:
        if shape.area() > best.area():
            best = shape
    return best
