import math
from .base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        # Проверяем существует ли треугольник с такими сторонами
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Невозможно построить треугольник с такими"
                             " сторонами")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        """
        Метод вычисления площади треугольника
        :return: значение площади
        """
        # Вычисляем площадь по формуле Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def is_right_triangle(self) -> bool:
        """
        Метод-свойство проверки треугольника на прямоугольность
        :return: True если прямоугольный, False если нет
        """
        # Сортируем стороны по возрастанию, чтобы в конце кортежа оказалась
        # гипотенуза
        sides = sorted((self.a, self.b, self.c))

        # Вычисляем разницу квадрата гипотенузы и суммы квадратов катетов (для
        # прямоугольного треугольника она должна
        # быть 0)
        # Учитываем что работаем с float и проверяем что разница меньше порога
        # точности
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9
