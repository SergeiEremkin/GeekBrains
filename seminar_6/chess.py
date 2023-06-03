# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random


def make_desk(size: int) -> list[[int]]:
    EMPTY = 0
    return [[EMPTY for _ in range(size)] for _ in range(size)]


def show_desk(desk: list[[int]]) -> None:
    print()
    print(*desk, sep='\n')



def feel_desk(desk: list[[int]], queens: list(())) -> list[[int]]:
    '''
    Функция заполняет доску ферзями.
    1 - ферзь на поле, 0 - поле пустое
    Возвращает доску в виде списка с расставленными фигурами
    '''
    BUSY = 1
    for i in range(len(queens)):
        desk[queens[i][0]][queens[i][1]] = BUSY
    return desk


def _check_turns(desk: list[[int]]) -> bool:
    counter = 0
    for col in desk:
        for el in col:
            if el == 1:
                counter += 1
        if counter > 1:
            return False
        else:
            counter = 0
    return True


def _transparent(desk: list[[int]]) -> bool:
    return [[*col] for col in zip(*desk)]


def _make_all_diagonal(desk: list[[int]]) -> bool:
    n = len(desk)  # размер квадратной матрицы
    all_diags = []  # здесь будут храниться все найденные
    #     побочные диагонали
    main, second = _check_main_diagonal(desk)
    all_diags.append(main)
    all_diags.append(second)
    for distance in range(1, n):  # distance - расстояние от главной диагонали
        sum_tl = n - 1 - distance  # сумма индексов (верхний-левый угол)
        sum_br = n - 1 + distance  # сумма индексов (нижний-правый угол)
        all_diags.extend([
            [desk[i][sum_tl - i] for i in range(n - distance)],  # верх-лев диаг
            [desk[i][sum_br - i] for i in range(distance, n)]  # ниж-прав диаг
        ])

    return all_diags  # возвращаем все побочные диагонали


def is_beat(size: int, queens: list(())) -> bool:
    desk = make_desk(size)
    desk_with_queens = feel_desk(desk, queens)
    if _check_turns(desk_with_queens):
        rotate_desk = _transparent(desk_with_queens)
        if _check_turns(rotate_desk):
            diagonal_desk = _make_all_diagonal(desk_with_queens)
            if _check_turns(diagonal_desk):
                return True
    return False


def _check_main_diagonal(desk: list[[int]]) -> bool:
    main_diag = [desk[i][i] for i in range(len(desk))]
    secondary_diagonal = [desk[i][len(desk) - i - 1] for i in range(len(desk))]
    return [main_diag, secondary_diagonal]


def generate_queens_coordinates() -> list[()]:
    LENGTH_COORDINATES = 8
    coordinates = []
    i = 0
    while i <= LENGTH_COORDINATES - 1:
        x, y = random.randint(0, 7), random.randint(0, 7)
        if (x, y) not in coordinates:
            coordinates.append((x, y))
            i += 1
    return coordinates


def show_success() -> None:
    SIZE = 8
    count = 4
    while count > 0:
        coord_queens = generate_queens_coordinates()
        result = is_beat(SIZE, coord_queens)
        if result:
            desk_with_queens = feel_desk(make_desk(SIZE), coord_queens)
            show_desk(desk_with_queens)
            print(result)
            count -= 1


if __name__ == "__main__":
    desk_1 = make_desk(8)
    desk_2 = make_desk(8)
    queens = [(0, 0), (1, 1), (0, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
    desk_with_queens_1 = feel_desk(desk_1, queens)
    show_desk(desk_with_queens_1)
    print(is_beat(8, queens))
    print()
    queens_2 = [(0, 3), (1, 1), (2, 7), (3, 4), (4, 6), (5, 0), (6, 2), (7, 5)]
    desk_with_queens_2 = feel_desk(desk_2, queens_2)
    show_desk(desk_with_queens_2)
    print(is_beat(8, queens_2))
    # generate = generate_queens_coordinates()
    # show_desk(generate)
    show_success()
