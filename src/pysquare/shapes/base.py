from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Базовый абстрактный класс для всех фигур.
    """
    @abstractmethod
    def area(self, *args, **kwargs) -> float:
        """Метод для вычисления площади фигуры."""
        ...
