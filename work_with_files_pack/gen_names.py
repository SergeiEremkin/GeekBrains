# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnqrstvwxz'


def name_gen(count: int, str_len_min: int, str_len_max: int, file_2: Path) -> None:
    with open(file_2, 'a', encoding='utf-8') as f_2:
        for _ in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                 for i in range(randint(str_len_min, str_len_max)))
            f_2.write(f'{rad_string.capitalize()}\n')