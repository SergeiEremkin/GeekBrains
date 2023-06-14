# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random
from cmath import sqrt
from typing import Callable


def find_root_in_csv_deco(func: Callable) -> object:
    def wrapper(*args, **kwargs):
        equations = {}
        with open('odds.csv', 'r') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            equation = {}
            for row in reader:
                if count > 0:
                    equation = {count: {'a': int(row[0]),
                                        'b': int(row[1]),
                                        'c': int(row[2]),
                                        'result': func(int(row[0]), int(row[1]), int(row[2]))}}
                equations.update(equation)
                count += 1
        return equations

    return wrapper


def write_json(func: Callable):
    def wrapper(*args, **kwargs):
        result = func()
        print(result)
        with open('odds.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    return wrapper


@write_json
@find_root_in_csv_deco
def find_root(a: int = 1, b: int = 1, c: int = 1) -> tuple[str, str] | str:
    discriminant = (pow(b, 2)) - (4 * a * c)
    if discriminant < 0:
        return f'нет действительных корней'
    if discriminant == 0:
        return str(-b / (2 * a))
    else:
        if a != 0:
            return str((-b + sqrt(discriminant)) / (2 * a)), str((-b - sqrt(discriminant)) / (2 * a))


def generate_numbers() -> None:
    MIN_NUM = 1
    MAX_NUM = 9
    MIN_LEN = 1
    MAX_LEN = 5
    generated_num = ''
    rnd_len = random.randint(MIN_LEN, MAX_LEN)
    for _ in range(1, rnd_len + 1):
        generated_num += str(random.randint(MIN_NUM, MAX_NUM))
    return int(generated_num)


def make_line() -> str:
    COUNT_NUMS = 3
    for i in range(COUNT_NUMS):
        yield str(generate_numbers())


def write_csv(file: str) -> None:
    LINE_COUNT = 100
    list_csv = []
    for _ in range(LINE_COUNT):
        num_1, num_2, num_3 = make_line()
        list_csv.append([num_1, num_2, num_3])
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        writer.writerows(list_csv)


if __name__ == '__main__':
    write_csv('odds.csv')
    find_root()
