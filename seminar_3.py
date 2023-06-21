# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков
import unittest


# def solution_1(array: list[int]) -> list[int]:
#     res = []
#     for i in range(len(array)):
#         if array[i] not in res:
#             res.append(array[i])
#     return res
#
#
# print(solution_1([2, 2, 3, 4, 5, 5, 6, 6]))
#
#
# def solution_2(array: list[int]) -> list[int]:
#     return list(set(array))
#
#
# print(solution_2([2, 2, 3, 4, 5, 5, 6, 6]))


# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях


# def task2():
#     input_data = input("Enter data: ")
#     if input_data.isdigit():
#         result = int(input_data)
#     elif (input_data.count(".") == 1 or (input_data.count("-") == 1
#                                          and input_data.startswith("-"))) \
#             and (input_data.replace("-", "").replace(".", "").isdigit()):
#         result = float(input_data)
#     elif not input_data.islower():
#         result = input_data.lower()
#     else:
#         result = input_data.upper()
#     print(f"{result}")
#
#
# task2()

# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где
# ключ - тип элемента,
# значение - список элементов данного типа

# def task3():
#     input_tuple = (3, 5, "asd", True, 5.45, False, "jlh", 8.4)
#     result_dict = {}
#     for i in input_tuple:
#         if type(i) not in result_dict.keys():
#             result_dict[type(i)] = []
#         result_dict[type(i)].append(i)
#     print(result_dict)
#
# task3()


# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.


# def task4(array: list[int]) -> list[int]:
#     for item in set(array):
#         count = array.count(item)
#         if count > 1:
#             for i in range(count):
#                 array.remove(item)
#     return array
#
# print(task4([2,2,3,4,4,4,5,6,7,7]))


# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы
def task5(array):
    res = []
    for i, elem in enumerate(array, start=1):
        if elem % 2:
            res.append(i)
    return res


print(task5([2, 2, 3, 4, 4, 4, 5, 6, 7, 7]))


class TestMethods(unittest.TestCase):

    def test_task5(self):
        self.assertEqual(task5([2, 2, 3, 4, 4, 4, 5, 6, 7, 7]), [3, 7, 9, 10])


if __name__ == '__main__':
    unittest.main()

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


# def task6():
#     input_data = input("Enter your data: ")
#     words_list = input_data.split()
#     max_length = len(words_list[0])
#     for i in words_list:
#         if len(i) > max_length:
#             max_length = len(i)
#
#     words_list.sort()
#     for num_line, line in enumerate(words_list, start=1):
#         print(f"{num_line} {line:>{max_length}}")
#
#
# task6()
