# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны
from puzzle_mistery_with_dict import save_statistic


def puzzle(question: str, answers: list[str], limit: int) -> str:
    count = 1
    is_win = True
    while limit > count:
        user_input = input(f'Отгадайте загадку: {question}: ')
        if user_input in answers:
            save_statistic(question, count)
            return f'Поздравляю. Вы отгадали с {count} попытки'
        else:
            is_win = False
            count += 1
    if not is_win:
        save_statistic(question, count)
        return f'У вас осталось 0 попыток. К сожалению вы не угадали.'
