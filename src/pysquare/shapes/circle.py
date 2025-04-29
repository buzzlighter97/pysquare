import math
from .base import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
