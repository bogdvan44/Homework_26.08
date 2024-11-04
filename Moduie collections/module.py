from collections import Counter
from collections import defaultdict
from collections import OrderedDict

def count_elements(lst):
    return Counter(lst)
my_list = [6, 1, 2, 2, 3, 1, 4, 4, 4, 4, 5, 5, 2]
# выбираем каждый уникальный элемт с количеством повторений
result = count_elements(my_list)
print(result)

def tuples_defaultdict(tuples_list):
    result = defaultdict(list)

    for key, value in tuples_list:
        result[key].append(value)
    return result
# Возвращаем словарь где ключ (1-й элемент кортежа), значение (второй элемент в списке)
tuples_list = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
result = tuples_defaultdict(tuples_list)
print(result)

def list_ordered_dict(lst):
    result = OrderedDict()

    for index, value in enumerate(lst):
        result[value] = index
    return result
# Возвращаем словарь где ключ (элемент списка), а значение (его индекс)
my_list = ['one', 'two', 'three', 'one', 'four', 'five']
result = list_ordered_dict(my_list)
print(result)


def filter_defaultdict(dd, threshold):
    # Создаем новый defaultdict
    filtered_dd = defaultdict(list)
    # Проходим по элементам исходного defaultdict
    for key, value in dd.items():
        # Проверяем, больше ли значение от заданного threshold = 3
        if value > threshold:
            filtered_dd[key] = value
    return filtered_dd
# Пример использования
dd = defaultdict(int, {'a': 1, 'b': 4, 'c': 2, 'd': 5, 'e': 6, 'f': 3})
threshold = 3
result = filter_defaultdict(dd, threshold)
print(result)

