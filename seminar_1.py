# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


CHECK_NORMAL_1 = 4
CHECK_NORMAL_2 = 100
CHECK_NORMAL_3 = 400
START_YEAR = 1582
result = ''
year = int(input('Введите год: '))
if year < START_YEAR:
    result = 'Вы ввели не верную дату'
elif year % CHECK_NORMAL_1:
    result = 'Год обычный'
elif not year % CHECK_NORMAL_2:
    if not year % CHECK_NORMAL_3:
        result = 'Високосный'
    else:
        result = 'Обычный'
else:
    result = 'Високосный'
print(result)

# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


FROM = 1
TO = 999
result = None
while True:
    number = input(f"Введите число от {FROM} до {TO}: ")
    if FROM <= int(number) <= TO:
        match len(number):
            case 1:
                result = int(number) ** 2
            case 2:
                result = int(number) % 10 * int(number) // 10
            case 3:
                result = number[::-1]
        break
print(result)

# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки?
#    *
#    ***
#   *****
#  *******
# *********


rows = int(input("Сколько рядов у ёлки? "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.


MIN = 2
MAX_1 = 9
MAX_2 = 10
for i in range(MIN, MAX_1 + 1):
    for j in range(MIN, MAX_2 + 1):
        print(f'{i} x {j} = {i * j}')
    print(' ')
