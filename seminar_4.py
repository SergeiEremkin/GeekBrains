# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


# def show_string(text: str) -> list[int]:
#     str_list = text.split()
#     len_max = len(max(str_list, key=len))
#     for i, s in enumerate(str_list, start=1):
#         print(f'{i} {s:>{len_max}}')
#
#
# show_string('привет, как дела?')

# [print(f"{i} - {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]


# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию


def unique_unicode(text: str) -> list[int]:
    res = set()
    for s in text:
        res.add(ord(s))
    str_list = sorted(res, reverse=True)
    return str_list


# print(unique_unicode('привет, как дела?'))


# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно


def convert_text(text: str) -> dict[int]:
    res = {}
    splited_text = sorted([int(i) for i in text.split()])
    for i in range(splited_text[0], splited_text[1] + 1):
        res[chr(i)] = i
    return res


print(convert_text('501 626'))


# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии


def bubble_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1 - i):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(bubble_sort([2, 1, 3, 6, 1, 2]))


# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def calc_bonus(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {names: salary / 100 * bonus
            for names, salary, bonus in zip(names, salary, (float(i[:-1]) for i in bonus))}


print(calc_bonus(['вася', 'петя', 'коля'], [10000, 20000, 30000], ['12.5%', '15%', '10%']))


# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

def sum_numbers(numbers: list[int], index_min: int, index_max: int) -> int:
    if index_min > index_max:
        sum_numbers(numbers, index_max, index_min)
    if index_min < 0:
        index_min = 0
    if index_max > len(numbers) - 1:
        index_max = len(numbers) - 1

    return sum(numbers[index_min: index_max + 1])


print(sum_numbers([2, 3, 4, 6], 2, 1))


# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def check_profit(company: dict[str:[int]]) -> bool:
    for values in company.values():
        if sum(values) < 0:
            return False
    return True


print(check_profit({'компания1': [1000, -2000, 5000, -1000], 'компания2': [300, 5000, 200, 4000],
                    'компания3': [1000, 1000, -3000]}))


# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def replacement_with_s(*words):
    words = list(words)
    temp = []
    for i in range(len(words)):
        if words[i].endswith('s') and words[i] != 's':
            temp.append(words[i])
            words[i] = None
    for i in range(len(words)):
        if words[i] is not None:
            words[i] += ''.join([i for i in temp])
    return words


print(replacement_with_s('ноs', 'рот', 'насоs', 's'))
