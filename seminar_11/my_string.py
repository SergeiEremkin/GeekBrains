# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Добавьте к задачам 1 и 2 строки документации для классов.
import time


class MyString(str):
    '''Расширяемый класс str.'''

    def __new__(cls, value: str, name: str):
        '''Расширяеи метод new параметрами value и name.'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return self + " " + f'{self.name} {self.created_at}'


if __name__ == '__main__':
    mystr = MyString('САМА строка', 'доп. параметр')
    # print(mystr.name)
    # print(mystr.created_at)
    print(mystr)
    # print(mystr.upper())
    # help(mystr)
    # help(MyString)

