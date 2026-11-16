"""Polymorphism and abstract classes

Different shapes answer the same questions (area, perimeter) in different ways. Code that
only calls those methods works for any shape, including ones written later.

  Shape      abstract base class (ABC). Shape() itself must raise TypeError.
             abstract methods: area() and perimeter()
             concrete method:  describe() -> "<name>: area=<a:.2f>, perimeter=<p:.2f>"
                               where <name> is the class attribute `name` of the subclass
  Circle(radius)           name = "circle"
  Rectangle(width, height) name = "rectangle"
  Square(side)             name = "square"; build it by SUBCLASSING Rectangle
  largest(shapes) -> the shape with the greatest area (the first one if tied).
                     Raise ValueError for an empty list.

Every size must be greater than zero, else ValueError.

Concepts: abstract base classes (abc), polymorphism, inheritance used for a real "is a"
relationship, the open/closed idea (largest() needs no change when a new shape appears).
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    name = "shape"

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        raise NotImplementedError


class Circle(Shape):
    name = "circle"

    def __init__(self, radius: float) -> None:
        raise NotImplementedError


class Rectangle(Shape):
    name = "rectangle"

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError


class Square(Rectangle):
    name = "square"

    def __init__(self, side: float) -> None:
        raise NotImplementedError


def largest(shapes: list) -> Shape:
    raise NotImplementedError
