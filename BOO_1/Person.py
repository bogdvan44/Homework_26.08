class Person:
    # Создаем class человек с определенными атрибутами
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
    # используем декоратор для получения значения
    @property
    def name(self):
        return self._name
    # используем @setter для установки нового значения
    @name.setter
    def name(self, new_name):
        self._name = new_name
    # используем декоратор для получения значения
    @property
    def age(self):
        return self._age
    # используем @setter для установки нового значения
    @age.setter
    def age(self, new_age):
        self._age = new_age
    # используем декоратор для получения значения
    @property
    def height(self):
        return self._height
    # используем @setter для установки нового значения
    @height.setter
    def height(self, new_height):
        self._height = new_height

person = Person("Kevin", 44, 180)
print(person.name)
print(person.age)
print(person.height)

person.name = "Alex"
person.age = 34
person.height = 178

print(person.name)
print(person.age)
print(person.height)

