# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def long(self):
        return 2 * pi * self.r

    def area(self):
        return pi * pow(self.r, 2)


if __name__ == '__main__':
    circle = Circle(5)
    print(f'{circle.long()= } {circle.area()= }')
