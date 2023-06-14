# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
from typing import Callable


def deco_json(func: Callable):
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        final_dict.update({str(res): args})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)

    return wrapper



def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


multy(2, 5, temp=2, res=3, c=2, d=5)
