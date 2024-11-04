
class Book:
    def __init__(self, name, author, pages, year):
        self.n = name   # Название книги
        self.a = author # Автор
        self.p = pages  # Количество страниц
        self.y = year   # Год издания

    def __str__(self):
        return (f"Name: {self.n}, Author: {self.a}, "
                f"Pages: {self.p}, Year of issue: {self.y}г.")

book = Book("Life after 40", "Bogdan", "222", "2025")
print(book)


class Student:
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name    # Имя
        self.last_name = last_name      # Фамилия
        self.age = age                  # Возраст
        self.grades = grades            # Оценки за учебный год (список)

    def calculate_average(self):
        # Метод для подсчета среднего балла.
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_achievements(self):
        # Метод для получения информации о достижениях.
        average = self.calculate_average()
        if average >= 9:
            return f"{self.first_name} {self.last_name} - Отличник"
        elif average >= 7:
            return f"{self.first_name} {self.last_name} - Хорошист"
        elif average >= 6:
            return f"{self.first_name} {self.last_name} - Учащийся"
        else:
            return f"{self.first_name} {self.last_name} - Неудовлетворительно"

# Пример использования класса
student1 = Student("Иван", "Богдан", 44, [7, 9, 8, 6, 7, 8, 7])
print(f"Средний балл: {student1.calculate_average()}")
print(student1.get_achievements())


class Auto:
    def __init__(self, brand, model, year, color, transmission):
        self.b = brand
        self.m = model
        self.y = year
        self.c = color
        self.t = transmission

    def __str__(self):
            return (f"Brand: {self.b} Model: {self.m} "
                    f"Year: {self.y} Color: {self.c} Transmission: {self.t}")

    def start_engine(self):
        return ("Завести двигатель")

car = Auto("KIA", "Sorento", "2003", "Grey", "Automatic")
print(car)
print(car.start_engine())


class Refrigerator:
    def __init__(self, manufacturer, capacity, model_name):
        self.man = manufacturer # Производитель
        self.cap = capacity # Емкость (в литрах)
        self.mod = model_name # Модель
        self.is_open = False  # Состояние дверцы (открыта или закрыта)
        self.is_on = False  # Состояние устройства (включено или выключено)
        print(f"Холодильник: {self.man}, Ёмкость: {self.cap}l, Модель: {self.mod}")

    def open_door(self):
            print(f"Дверца холодильника {self.mod} открыта.")

    def close_door(self):
            print(f"Дверца холодильника {self.mod} закрыта.")

    def turn_on(self):
            print(f"Холодильник {self.mod} включен.")

    # Пример использования
Indesit = Refrigerator("Indesit", "278", "Indesit ES 16")
Indesit.turn_on()
Indesit.open_door()
Indesit.close_door()


class Human:
    def __init__(self, name, surname, age, phone):
        self.name = name       # Имя
        self.surname = surname # Фамилия
        self.age = age         # Возраст
        self.phone = phone     # Телефон

    def __str__(self):
        return (f"Name: {self.name}, Surname: {self.surname},  "
                     f"Age: {self.age}, Phone: {self.phone}.")

    def stand_up(self):
            print(f"{self.name} (Команда встать)")

    def sit_down(self):
            print(f"{self.name} (Команда сесть)")


human = Human("Ivan", "Bogdan", "44", "1336567")
print(human)
human.stand_up()
human.sit_down()


class House:
    def __init__(self, floors, square, rooms, price):
        self.floors = floors # Количество этажей
        self.square = square # Площадь
        self.rooms = rooms   # Комнаты
        self.price = price   # Стоимость

    def calculate_price(self):
            """Метод для расчета стоимости дома."""
            total_price = self.square * self.price
            return total_price

    def display_info(self):
            """Метод для вывода информации о доме."""
            print(f"Дом с {self.floors} этажами, площадью {self.square} м² и {self.rooms} комнатами.")
            print(f"Стоимость дома: {self.calculate_price()} у.е.")

    # Пример использования
my_house = House(floors=2, square=130, rooms=6, price=1050)
my_house.display_info()




