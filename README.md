# Модуль pysquare

Небольшой модуль Python для работы с числовыми свойствами геометрических фигур.  
В настоящее время поддерживает:

- **Circle**: площадь круга по радиусу  
- **Triangle**: площадь треугольника по длинам сторон (формула Герона) и проверка на прямой угол

---

## Установка

Распакуйте архив или установите как пакет:
   ```bash
   unzip pysquare.zip
   cd pysquare
   pip install .
   ```
---

## Быстрый старт

```python
from shapes import Circle, Triangle

# Вычисление площади круга
c = Circle(radius=2.5)
print(f"Площадь круга: {c.area():.2f}")
# => Площадь круга: 19.63

# Вычисление площади треугольника
t = Triangle(a=3, b=4, c=5)
print(f"Площадь треугольника: {t.area():.2f}")
# => Площадь треугольника: 6.00

# Проверка на прямой угол
print("Прямой угол?", t.is_right)
# => Прямой угол? True

# Смешанный список фигур
objs = [Circle(1), Triangle(5,12,13)]
for obj in objs:
    print(f"{type(obj).__name__}: {obj.area()}")
```

---

## Справочник API

### `class shapes.base.Shape`

Абстрактный базовый класс. Все конкретные фигуры должны наследоваться от `Shape` и реализовывать метод:

```python
def area(self) -> float
```

### `shapes.base.area(shape: Shape) -> float`

Универсальная функция, вызывающая `shape.area()`.

### `class shapes.circle.Circle(radius: float)`

- **Конструктор**: `radius` — радиус круга  
- **Метод**: `area() → float`

### `class shapes.triangle.Triangle(a: float, b: float, c: float)`

- **Конструктор**: три длины сторон (`a`, `b`, `c`).  
  Вызывает `ValueError`, если стороны не образуют треугольник.  
- **Метод**: `area() → float` (формула Герона)  
- **Свойство**: `is_right → bool` — проверяет, является ли треугольник прямоугольным

---

## Запуск тестов

Модуль включает тесты `pytest`:

```bash
pip install pytest
pytest -q
```

Тесты проверяют:

- Корректные вычисления площадей круга и треугольника  
- Ошибку для некорректного треугольника  
- Детекцию прямого угла  
- Расширяемость через реестр  

---

## Расширение новыми фигурами

Чтобы добавить свою фигуру:

1. **Наследуйтесь** от `Shape` в каталоге `shapes/` и реализуйте `area(self) -> float`.  
3. Теперь вы можете вызывать `obj.area()` без правки существующего кода.

```python
from shapes.base import Shape, area

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

s = Square(4)
print(s.area())  # 16.0
```

---

## Лицензия

MIT License
