import fractions


# Решить задачи, которые не успели решить на семинаре.
#
#
#
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "bin":
            convert = 2
        case "oct":
            convert = 8
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'a'
            if res == 11:
                res = 'b'
            if res == 12:
                res = 'c'
            if res == 13:
                res = 'd'
            if res == 14:
                res = 'e'
            if res == 15:
                res = 'f'
        result += str(res)
        num = num // convert
    return result[::-1]


print(convert_number(21, mode="bin"), f"assert: {bin(21)}")
print(convert_number(21, mode="oct"), f"assert: {oct(21)}")
print(convert_number(1200, mode="hex"), f"assert: {hex(1200)}")


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


def converter_to_int(frac_1: list[str, str], frac_2: list[str, str]) -> None:
    i = 0
    while i < len(frac_1):
        frac_1[i] = int(frac_1[i])
        frac_2[i] = int(frac_2[i])
        i += 1


def reduction_fraction(frac: list[int, int]) -> list[int, int]:
    i: int = 2
    if frac[0] < frac[1]:
        x = frac[0]
    else:
        x = frac[1]
        if frac[0] % frac[1] == 0:
            result = int(frac[0]) / int(frac[1])
    while i <= x:
        if frac[0] % i == 0 and frac[1] % i == 0:
            frac[0] /= i
            frac[1] /= i
            continue
        i += 1
    return [int(frac[0]), int(frac[1])]


def sum_fraction(frac_1: list[int, int], frac_2: list[int, int]) -> list[int, int]:
    if frac_1[1] == frac_2[1]:
        result = [frac_1[0] + frac_2[0], frac_1[1]]
    else:
        nok = frac_1[1] * frac_2[1]
        result = [frac_1[0] * frac_2[1] + frac_2[0] * frac_1[1], nok]
    return result


def multy_fraction(frac_1: list[int, int], frac_2: list[int, int]) -> list[int, int]:
    return [frac_1[0] * frac_2[0], frac_1[1] * frac_2[1]]


def show_result(res: list[int, int]):
    if res[0] == res[1]:
        return f'{res[0] / res[1]}'
    else:
        return f'{res[0]}/{res[1]}'


def fraction_start(fr_1: str, fr_2: str) -> ([int, int], []):
    frac_1 = fr_1.split('/')
    frac_2 = fr_2.split('/')
    converter_to_int(frac_1, frac_2)
    sum_res = reduction_fraction(sum_fraction(frac_1, frac_2))
    print(f'{frac_1[0]}/{frac_1[1]} + {frac_2[0]}/{frac_2[1]} = {show_result(sum_res)}')
    multy_res = reduction_fraction(multy_fraction(frac_1, frac_2))
    print(f'{frac_1[0]}/{frac_1[1]} * {frac_2[0]}/{frac_2[1]} = {show_result(multy_res)}')


fraction_start('1/2', '2/3')

print('\nПроверка с помощью модуля "fractions":')
f1 = fractions.Fraction(1, 2)
f2 = fractions.Fraction(2, 3)
print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')
