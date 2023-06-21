# Решить задачи, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    '''Класс матрица с инициализацией списка списков,с переопределенными
     методами сложения и умножения и строчного вывода.'''

    def __init__(self, list_of_lists: list[list[int]]):
        '''Инициализация инит с аргументом list[list[int]].'''
        self.list_of_lists = list_of_lists

    def __str__(self):
        'Вывод списка списков построчно.'
        result = ''
        for row in self.list_of_lists:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        '''Переопределённый метод для сравнения матриц.
        Матрицы могут быть равны когда равны их длины и каждый элемент.'''
        return True if self.list_of_lists == other.list_of_lists else False

    def __add__(self, other):
        '''Переопределил метод поэлементного сложения матриц.
        Можно складывать матрицы одинаковой длины строки первой и столбца второй. '''
        result = []
        row = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        '''Переопределенный метод умножения матриц.
        Можно складывать матрицы одинаковой длины строки первой и столбца второй.'''
        m = len(self.list_of_lists)
        n = len(other.list_of_lists)
        k = len(other.list_of_lists[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.list_of_lists[i][k] * other.list_of_lists[k][j] for k in range(n))
        return Matrix(result)


if __name__ == '__main__':
    matrix_1 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_2 = Matrix([[3, 3, 3], [3, 3, 3], [3, 3, 3]])
    matrix_sum = matrix_1 + matrix_2
    print(matrix_sum)
    matrix_mul = matrix_1 * matrix_2
    print(matrix_mul)
    if matrix_1 == matrix_2:
        print('True')
    else:
        print('False')
