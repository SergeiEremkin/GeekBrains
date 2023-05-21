from math import pi
import decimal

# Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.

# a = 1
# b = 'строка'
# c = 0.3
# d = (1, 1)
# e = {1: 3}
# print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}, d - {type(d)}, e - {type(e)} ')

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты

# data = [a, b, c, d, 1, 'строка']
# for i, el in enumerate(data, start=1):
#     print(i, el, id(el), el.__sizeof__(), hash(el))
#     if isinstance(el, int):
#         print('Это целое число')
#     elif isinstance(el, str):
#         print('Это строка')


# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
#
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

def task3(num: int, mode: str) -> str:
    result = ''
    convert: int = 2

    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8

    while num >= 1:
        res = num % convert

        result += str(res)
        num = num // convert

    return result[::-1]


print(task3(21, mode="bin"), f"assert: {bin(21)}")
print(task3(21, mode="oct"), f"assert: {oct(21)}")


# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
#
# ✔ Диаметр не превышает 1000 у.е.
#
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.


def circle(d: decimal) -> tuple[decimal, decimal]:
    decimal.getcontext().prec = 42
    _pi = decimal.Decimal(pi)
    if d <= 1000:
        s = (_pi * d**2) / 4
        l = _pi * d

    return decimal.Decimal(s), decimal.Decimal(l)

# 5) Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.


# def quadratic_equation():
#     print('Решаем уравнение a•x²+b•x+c=0')
#     a = input('Введите значение a: ')
#     b = input('Введите значение b: ')
#     c = input('Введите значение c: ')
#     a = float(a)
#     b = float(b)
#     c = float(c)
#     discriminant = b ** 2 - 4 * a * c
#     print('Дискриминант = ' + str(discriminant))
#     if discriminant == 0:
#         x = -b / (2 * a)
#         print('x = ' + str(x))
#     else:
#         x1 = (-b + discriminant ** 0.5) / (2 * a)
#         x2 = (-b - discriminant ** 0.5) / (2 * a)
#         print('x₁ = ' + str(x1))
#         print('x₂ = ' + str(x2))

#quadratic_equation()

# 6) Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


class Bank:

    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION

        _MAX = 600
        _MIN = 30

        if sum_commission > _MAX:
            return _MAX
        elif sum_commission < _MIN:
            return _MIN
        else:
            return int(sum_commission)

    def _check_operation(self):
        return (False, True)[self._OPERATION % 3]

    def _check_tax(self):
        _MAX = 5_000_000
        return (False, True)[self._BALANCE >= _MAX]

    def _exit(self):
        return "Всего доброго, приходите к нам еще"

    def start(self, mode: str, cash: int = 0) -> str:

        check_operation = self._check_operation()
        check_tax = self._check_tax()

        if check_operation:
            self._BALANCE += self._BALANCE * self._BONUS

        elif check_tax:
            self._BALANCE -= self._BALANCE * self._TAX

        match mode:
            case "in":
                data = self._in(cash=cash)

                com_data = self._check_commission(cash=cash)

                return f"Средства были зачислены сумма: {cash}, баланс: {self._BALANCE}"

            case "out":
                com_data = self._check_commission(cash=cash)

                data = self._out(cash=cash, commission=com_data)

                if data:
                    return f"Операция осуществлена успешно, сумма: {cash}, коммисия: {com_data}, баланс: {self._BALANCE}"
                else:
                    return "Нехватает средств"

            case "exit":
                return self._exit()

bank = Bank()
print(bank.start(mode='in', cash=5_000_001))

