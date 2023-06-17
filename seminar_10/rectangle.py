# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, a: int, b: int = None):
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    rect = Rectangle(5)
    rect_1 = Rectangle(5, 10)
    print(f'{rect.perimeter()= } {rect.area()= }')
    print(f'{rect_1.perimeter()= } {rect_1.area()= }')
