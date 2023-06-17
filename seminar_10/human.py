# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст


class Human:

    def __init__(self, firstname: str, lastname: str, age: int, gender: str):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.get_age()} {self.gender}'






if __name__ == '__main__':
    h_1 = Human('Иван', 'Иванов', 23, 'мужской')
    h_2 = Human('Петр', 'Сидоров', 40, 'мужской')
    print(h_1)
    print(h_2)
    h_1.birthday()
    h_2.birthday()
    print(h_1)
    print(h_2)
