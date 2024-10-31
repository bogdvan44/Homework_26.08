
def sort_students_by(students):
    # Сортируем список словарей по ключу 'возраст' в порядке убывания
    sorted_students = sorted(students, key=lambda student: student['возраст'], reverse=True)
    return sorted_students
# Пример
students_list = [
    {'имя': 'Яросла', 'возраст': 42, 'оценки': [5, 4, 5]},
    {'имя': 'Артур', 'возраст': 27, 'оценки': [4, 5, 5]},
    {'имя': 'Иван', 'возраст': 44, 'оценки': [4, 3, 4]},
    {'имя': 'Яна', 'возраст': 23, 'оценки': [5, 5, 4]},
]
# Вызываем функцию
sorted_list = sort_students_by(students_list)
print(sorted_list)