import math
import pytest
from src.pysquare.shapes import Shape, Circle, Triangle


def test_circle_area():
    circle = Circle(2)
    assert math.isclose(circle.area(), math.pi * 4)


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert pytest.approx(triangle.area()) == 6.0


def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_is_right():
    triangle = Triangle(5, 12, 13)
    assert triangle.is_right_triangle


def test_extensibility():
    # создаём новый класс Square ("квадрат" в данном случае) и проверяем работоспособность метода area
    class Square(Shape):
        def __init__(self, side): self.s = side
        def area(self): return self.s * self.s

    square = Square(4)
    assert square.area() == 16
