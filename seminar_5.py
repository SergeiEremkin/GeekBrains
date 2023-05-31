# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

text = '3/5/7/8/10/12/13'


def make_dict(text: str) -> dict[int:int]:
    first, second, third, *other = (int(i) for i in text.split('/'))
    return {second: first, third: tuple(other)}


# print(make_dict(text))


# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


def from_str_to_dict(text_2: str) -> dict[str:int]:
    return {k: ord(k) for k in text_2}


# print(from_str_to_dict('sdsdsdd'))


# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


def from_str_to_dict_2(text_2: str) -> dict[str:int]:
    res_iter = iter({k: ord(k) for k in text_2}.items())
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))
    print(next(res_iter))


# from_str_to_dict_2('sdsdsddfghjkl;zxcvbnm,')


# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


def gen_num() -> None:
    return (i for i in range(0, 101, 2) if i // 10 + i % 10 != 8)


# for i in gen_num():
#     print(i)


# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


def fizz_buzz() -> None:
    print(
        *('FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)))


# fizz_buzz()


# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


def mult_table():
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_lIMIT and k == i + COLUMN - 1 else \
                f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1 else \
                    f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
            for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
            for k in range(i, i + COLUMN)))


mult_table()


def product_table() -> iter:
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4

    for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN):
        for j in range(LOWER_LIMIT, UPPER_lIMIT + 1):
            for k in range(i, i + COLUMN):
                if j == UPPER_lIMIT and k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')


product_table()


# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


#def check_simple(n: int) -> (iter, int):
    #gen_simple = (False if n % i == 0 else for i in range(2, n + 1))


def prime_gen(n: int) -> (iter, int):
    primes_list = []
    current_number = 2
    while len(primes_list) < n:
        is_prime = True
        for num in primes_list:
            if current_number % num == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(current_number)
            yield current_number
        current_number += 1


def func_2(input_number):
    result = True
    for divider in range(2, input_number+1):
        if input_number % divider == 0:
            result = False  # при первом же делении нацело возвращаем не простое
            break
    yield result


def simple_numbers(number: int):
    yield 2
    for i in range(3, number + 1):
        simple = True
        for j in range(2, i - 1):
            if not i % j:
                simple = False
        if simple:
            yield i


print(*simple_numbers(20))