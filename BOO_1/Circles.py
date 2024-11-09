import math
# Создаем класс Круг с атрибутом радиус и его начальным значением
class Circle:
    def __init__(self, radius):
        self._radius = radius
    # используем декоратор для получения значения радуса
    @property
    def radius(self):
        return self._radius
    # используем @setter для установки нового значения радиуса
    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
    # считаем площадь круга
    def square(self):
        return math.pi * (self._radius ** 2)

circle = Circle (12)
print(f"Радиус: {circle.radius}")
print(f"Площадь: {circle.square()}")

circle.radius = 15
print(f"Новый радиус: {circle.radius}")
print(f"Новая площадь: {circle.square()}")
