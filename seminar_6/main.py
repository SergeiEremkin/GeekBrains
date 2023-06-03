from sys import argv
from puzzle_numbers import gen_fnc
from puzzle_mystery import puzzle as p
from puzzle_mistery_with_dict import new_puzzle, show_statistic
from leap_year import date_validator


if __name__ == '__main__':
    # gen_fnc(*[int(i) for i in argv[1:]])
    # print(p('Зимой и летом одним цветом', ['eль', 'ёлка', 'Елка', 'Ель'], 3))
    # puzzle_dict = {
    #     'Зимой и летом одним цветом': ['eль', 'ёлка', 'Елка', 'Ель'],
    #     'Красна девица, а коса на улице': ['морковь', 'морковка'],
    #     'Два кольца, два конца, в по середине гвоздик': ['ножницы']
    # }
    # print(new_puzzle(puzzle_dict, 3))
    # show_statistic()
    data = '12.01.1999'
    print(date_validator(data))
    print(date_validator(argv[1]))
