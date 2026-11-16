import math

import pytest

from shapes_polymorphism import Circle, Rectangle, Shape, Square, largest


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        Shape()


def test_circle():
    c = Circle(2)
    assert c.area() == pytest.approx(math.pi * 4)
    assert c.perimeter() == pytest.approx(2 * math.pi * 2)


def test_rectangle():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14


def test_square_is_a_rectangle():
    s = Square(5)
    assert isinstance(s, Rectangle)
    assert isinstance(s, Shape)
    assert s.area() == 25
    assert s.perimeter() == 20


def test_describe_uses_the_subclass_name():
    assert Rectangle(3, 4).describe() == "rectangle: area=12.00, perimeter=14.00"
    assert Square(2).describe() == "square: area=4.00, perimeter=8.00"
    assert Circle(1).describe() == "circle: area=3.14, perimeter=6.28"


@pytest.mark.parametrize("make", [lambda: Circle(0), lambda: Circle(-1), lambda: Rectangle(0, 2),
                                  lambda: Rectangle(2, -1), lambda: Square(0)])
def test_sizes_must_be_positive(make):
    with pytest.raises(ValueError):
        make()


def test_largest_picks_by_area_and_first_wins_ties():
    a, b, c = Rectangle(2, 3), Square(3), Rectangle(1, 9)
    assert largest([a, b, c]) is b  # 9 beats 6, ties with c (9): first wins
    assert largest([a]) is a


def test_largest_of_nothing_is_an_error():
    with pytest.raises(ValueError):
        largest([])


def test_new_shapes_work_without_changing_existing_code():
    class Triangle(Shape):
        name = "triangle"

        def __init__(self, base, height, a, b, c):
            self.base, self.height, self.sides = base, height, (a, b, c)

        def area(self):
            return 0.5 * self.base * self.height

        def perimeter(self):
            return sum(self.sides)

    t = Triangle(10, 10, 10, 10, 10)
    assert t.describe() == "triangle: area=50.00, perimeter=30.00"
    assert largest([Square(2), t]) is t
