import unittest

import pytest


# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.


class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'


class TestRectangle(unittest.TestCase):

    def setUp(self) -> Rectangle:
        self.rectangle_1 = Rectangle(2, 3)
        self.rectangle_2 = Rectangle(5, 10)
        self.rectangle_3 = Rectangle(5)

    def test_perimeter(self):
        self.assertEqual(self.rectangle_1.perimeter(), 10)

    def test_area(self):
        self.assertEqual(self.rectangle_2.area(), 50)

    def test_sum_rect(self):
        self.assertEqual((self.rectangle_1 + self.rectangle_2).perimeter(), 40)

    def test_str(self):
        self.assertEqual(self.rectangle_1.__str__(), 'Прямоугольник 2 x 3')


if __name__ == '__main__':
    # rect_1 = Rectangle(2, 5)
    #
    # rect_2 = Rectangle(5, 10)
    # print(rect_2)
    # # print(f'{rect.perimeter()= } {rect.area()= }')
    # # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    # res_sum = rect_1 + rect_2
    # print(res_sum.a, res_sum.b)
    # res_sub = rect_1 - rect_2
    # print(res_sub.a, res_sub.b)
    unittest.main(verbosity=True)
