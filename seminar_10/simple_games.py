import json
from typing import Callable


class Games:
    _COUNT_REPEAT = 3


    def guess_number(self, count_try: int, num: int) -> Callable[[], None]:
        '''
        Игра "Угадай-ка". Нужно угадать число за определенное кол-во попыток
        :param count_try: кол-во попыток
        :param num: число для отхадывания
        :return:
        '''

        def random_numbers():
            for i in range(1, count_try + 1):
                user_input = input('Введите число для отгадывания от 1 до 100: ')
                if int(user_input) == num:
                    print(f'Вы угадали с {i} попытки')
                    break
            else:
                print('Вы не угадали')

        return random_numbers

    def counter(param: int):
        '''
        Декоратор, который вызывает метод заданное число раз
        :return:
        '''

        def deco_c(func: Callable):
            my_list = []

            def wrapper(*args, **kwargs):
                for i in range(param):
                    result = func(*args, **kwargs)
                    my_list.append(result)
                return my_list

            return wrapper

        return deco_c

    @counter(_COUNT_REPEAT)
    def fact(self, num: int) -> int:
        '''
        Метод нахождения факториала
        :param num:
        :return:
        '''
        res = 1
        for i in range(1, num + 1):
            res *= i
        return res

    def deco_json(func: Callable):
        '''
        Декоратор, который записывает метод в json
        :return:
        '''
        FILE_NAME = 'multy.json'
        with open(f'{FILE_NAME}', 'r') as f:
            final_dict = json.load(f)
            print(final_dict)

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            final_dict.update({str(res): args})
            final_dict.update({**kwargs})
            with open(f'{FILE_NAME}', 'w') as f:
                json.dump(final_dict, f, indent=2)

        return wrapper

    @deco_json
    def multy(self, a: int, b: int, *args, **kwargs) -> int:
        return a * b


if __name__ == '__main__':
    games = Games()
    # g = games.guess_number(3, 4)
    # print(g())
    print(games.fact(4))
    print(games.multy(2, 3, res=1, xyz=25))
