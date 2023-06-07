import decimal
import fractions
import os
import shutil
import sys
from pathlib import Path

# STEP = 2 ** 1
# a = 5
# print(type(a))
# a = "hello world"
# print(type(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a))
# a = 5
# print(type(a), id(a))
# a = "hello world"
# print(type(a), id(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a), id(a))
# data = 'f'
# print(isinstance(data, int))
# #input_1 = int(input('Введите что нибудь'))
# #print(type(input_1), id(input_1), hash(input_1))
# print("Hello world!".__doc__)
# print(str.__doc__)
# help('Hello world')
# #help()
# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')
#
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP
# print(sys.getsizeof(10 ** 100))

# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# 17
# h = hex(num)
# print(b, o, h)
# LIMIT = 120
# ATTENTION = 'Внимание!'
#
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
# " до ста лет, но длинна строки не должна превышать " +\
# str(LIMIT) + ' символов.'
# print(text)

# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())
# inp = input('Введите что-нибудь: ')
# if inp.isdigit():
#     print(bin(int(inp)), oct(int(inp)), hex(int(inp)))
# else:
#     if inp.isascii():
#         print('Строка написана в ASCII')
#     else:
#         print('Не написана')

# pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)
#
# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)
# arr = list()
# print(arr)
# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#         print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
#
#     return data
#
# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = mutable(my_list)
# print(f'{my_list = }\t{new_list = }')


# def func(y: int) -> int:
#     global x
#     x += 100
#     print(f'In func {x = }') # Для демонстрации работы, но не  для привычки принтить из функции
#
#     return y + 1
#
# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')

# my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
# s_key = sorted(my_dict.items())
# s_value = sorted(my_dict.items(), key=lambda x: x[1])
# print(f'{s_key = }\n{s_value = }')

# print(ord('a'))
# print(chr(97))
#
#
# def func(a, b, c):
#     x = a + b
#     print(locals())
#     z = x + c
#     return z
#
# func(1, 2, 3)


# SIZE = 10
#
#
# def func(a, b, c):
#     x = a + b
#     print(globals())
#     z = x + c
#     return z
#
#
# print(globals())
# print(func(1, 2, 3))

# print(vars(int))

# data = {2: 'two', 3: 'tree', 4: 'four'}
#
# dict_list = {item: data[item] for item in data if item > 2}
# print(dict_list)

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')
#
# a, b, c = ("один", "два", "три",)
# print(f'{a} {b} {c=}')
#
# a, *b, c = {"один", "два", "три", "четыре", "пять"}
# print(f'{a=} {b=} {c=}')

# link = \
# 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-op \
# tional-or-keyword-parameters-from-one-function-to-another'
# prefix, *_, suffix = link.split('/')
#
# print(f'{prefix=}, {suffix=}')

# data = [2, 4, 6, 8, 10, ]
# print(*data, sep='\t')
#
# a = b = c = 0
# a += 42
# print(f'{a=} {b=} {c=}')
#
# a = b = c = {1, 2, 3}
# a.add(42)
# print(f'{a=} {b=} {c=}')

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
#
# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
#
# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(next(x))
# y = next(x)
# z = next(iter(y))
# print(z)

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')

# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1, res2, res3)

# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep='\n')

from sys import path
import random as rnd

# Path('test_dir').mkdir()
# Path('test_dir').rmdir()
# f = open('test.txt', 'w', buffering=64) #ставить кодировку, чтобы корректно отображался русский текст
# f.write('123')
# f.close()
# print(list(f))
# f = open('test.txt', 'r', encoding='cp1251', errors='replace')
# print(list(f))
# # f.close()
# with open('test.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))


# with open('test.txt', encoding='utf-8') as f1:
#     for line in f1:
#         print(line.replace('\n', ''))

# text = ['Дозапись строки', 'Еще одна запись']
#
# with open('test.txt', 'r+', encoding='utf-8') as f1:
#      for line in text:
#          f1.seek(5, 2)
#          print(f1.tell())
#          print(line,end='***\n###', file=f1)


# start = 10
# stop = 100
# with open('data.bin', 'bw+') as f:
#     for i in range(start, stop + 1):
#         f.write(str(i).encode('utf-8'))
#     if i % 3 == 0:
#         f.seek(-2, 1)
#     f.truncate(stop)
#     f.seek(0)
#     res = f.read(start)
#     print(res.decode('utf-8'))

print(Path.cwd())
file2 = Path.cwd()/'one'/'two'
print(f'{file2=}{file2}')
p = Path(Path.cwd())
for obj in p.iterdir():
    print(obj.is_dir())
    print(obj.is_file())
    print(obj.is_symlink())


for dir_name, dir_path, file_name in os.walk(os.getcwd()):
    print(f'{dir_name=}, {dir_path=}, {file_name=}')

# p = Path('test.txt')
# p.rename('my_test.txt')
shutil.copy('data.bin', 'new_folder')