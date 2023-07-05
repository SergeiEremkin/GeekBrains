import argparse
from random import randint
import logging

# Решить задачи, которые не успели решить на семинаре.


# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


FORMAT = "{levelname} - {asctime} - {funcName}: {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='check_triangle.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        logger.info(f'Треугольник {a}/{b}/{b} существует')
        if a == b == c:
            logger.info(f'Треугольник {a}/{b}/{b} равносторонний')
        elif a == b or b == c or c == a:
            logger.info(f'Треугольник {a}/{b}/{b} равнобедренный')

        else:
            logger.info(f'Треугольник {a}/{b}/{b} разносторонний')
    else:
        logger.error(f'Треугольника {a}/{b}/{b} не существует')


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


# def simple():
#     i = 2
#     counter = 0
#     NOT_SIMPLE = 1
#     MIN = 0
#     MAX = 100000
#     while True:
#         number = int(input('Введите число в диапозоне от 1 до 100000: '))
#         if MIN < number < MAX:
#             while i <= number - 1:
#                 if number % i == 0:
#                     counter += 1
#                 i += 1
#             if counter >= NOT_SIMPLE:
#                 print('Число составное')
#             else:
#                 print('Число простое')
#             break
#         else:
#             print('Недопустимое значение:')


# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint
# 	num = randint(LOWER_LIMIT, UPPER_LIMIT)

# def guess_number():
#     LOWER_LIMIT = 0
#     UPPER_LIMIT = 100
#     COUNT_TRY = 2
#     RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
#     is_win = True
#     for _ in range(COUNT_TRY + 1):
#         number = int(input('Введи число от 0 до 1000: '))
#         if number > RAND_NUMBER:
#             print('Ваше число БОЛЬШЕ загаданного')
#             is_win = False
#         elif number < RAND_NUMBER:
#             print('Ваше число МЕНЬШЕ загаданного')
#             is_win = False
#         else:
#             print('Вы выиграли!')
#             is_win = True
#     if not is_win:
#         print('К сожалению вы проиграли')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка треугольника")
    parser.add_argument("param", metavar="a b c", type=int, nargs=3, help="Введите a b c через пробел")
    args = parser.parse_args()
    check_triangle(*args.param)
# print()
# simple()
# print()
# guess_number()

# @Stanislav_prof
