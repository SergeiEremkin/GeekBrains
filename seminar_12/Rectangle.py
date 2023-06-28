# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__
from seminar_13.custom_errors import SideError

class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    __slots__ = ('_a', '_b')

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self._a = a
        self._b = b if b is not None else a

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise SideError(value)

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise SideError(value)

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


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    # rect_2 = Rectangle(5, 10)
    print(rect_1.a)

print(rect_1.b)
# rect_1.a = -1
rect_1.a = -10
print(rect_1)
# print(rect_2)
# # print(f'{rect.perimeter()= } {rect.area()= }')
# # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
# res_sum = rect_1 + rect_2
# print(res_sum.a, res_sum.b)
# res_sub = rect_1 - rect_2
# print(res_sub.a, res_sub.b)
