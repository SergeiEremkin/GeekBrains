# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.
import doctest
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


import json
import unittest

import pytest

from seminar_13.custom_errors import LevelError, AccessError


class User:
    '''
    test_eq
    >>> u1 = User(1, 1, "Виталий")
    >>> u2 = User(2, 1, "Виталий")
    >>> u1 == u2
    True
    '''

    def __init__(self, level: int, user_id: int, name: str):
        self.level = level
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __str__(self):
        return f'{self.level} {self.user_id} {self.name}'


class Access:
    '''
    test_read_json
    >>> access = Access()
    >>> access.data = [User(1, 1, "Андрей"), User(1, 2, "Петр"), User(2, 3, "Василий"), User(3, 4, "Артур"), User(3, 5, "Степан")]
    >>> access.read_json('data.json')
    {'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'}, '3': {'4': 'Артур', '5': 'Степан'}}
    >>> data = access.parse_data({'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'}, '3': {'4': 'Артур', '5': 'Степан'}})
    >>> print(*data)
    1 1 Андрей 1 2 Петр 2 3 Василий 3 4 Артур 3 5 Степан
    >>> access.enter_system(User(5, 5, "Админ"), 5, "Степан")
    Traceback (most recent call last):
    seminar_13.custom_errors.LevelError: В доступе отказано. Ваш уровень ниже 5
    >>> access.enter_system(User(3, 5, "Админ"), 3, "Иван")
    Traceback (most recent call last):
    seminar_13.custom_errors.AccessError: Пользователя с id: 3 и с именем: Иван в базе не найдено
    '''

    def __init__(self):
        FILE_NAME = 'data.json'
        data = self.read_json(FILE_NAME)
        user_list = self.parse_data(data)
        self.data = user_list

    def read_json(self, file_name: str):

        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def parse_data(self, data: dict) -> list[User]:
        user_list = []
        for level, dict_users in data.items():
            for user_id, name in dict_users.items():
                user_list.append(User(int(level), int(user_id), name))
        return user_list

    def enter_system(self, super_user: User, user_id: int, name: str):
        temp_user = User(level=0, user_id=user_id, name=name)
        access_level = 0
        if temp_user in self.data:
            for user in self.data:
                if temp_user == user:
                    access_level = user.level
        else:
            raise AccessError(temp_user.user_id, temp_user.name)
        if access_level < super_user.level:
            raise LevelError(super_user.level)


@pytest.fixture()
def make_access():
    access = Access()
    access.data = [User(1, 1, "Андрей"), User(1, 2, "Петр"), User(2, 3, "Василий"), User(3, 4, "Артур"),
                   User(3, 5, "Степан")]
    return access


def test_read_json(make_access):
    assert make_access.read_json('data.json') == \
           {'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'}, '3': {'4': 'Артур', '5': 'Степан'}}


def test_parse_data(make_access):
    assert make_access.parse_data({'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'},
                                   '3': {'4': 'Артур', '5': 'Степан'}}) == [User(1, 1, "Андрей"),
                                                                            User(1, 2, "Петр"),
                                                                            User(2, 3, "Василий"),
                                                                            User(3, 4, "Артур"),
                                                                            User(3, 5, "Степан")]


def test_compare_users():
    u1 = User(1, 1, "Виталий")
    u2 = User(2, 1, "Виталий")
    assert u1 == u2


def test_enter_system_level_error(make_access):
    with pytest.raises(LevelError):
        make_access.enter_system(User(5, 5, "Админ"), 5, "Степан")


def test_enter_system_access_error(make_access):
    with pytest.raises(AccessError):
        make_access.enter_system(User(3, 5, "Админ"), 3, "Иван")


class TestAccess(unittest.TestCase):

    def setUp(self) -> None:
        self.access = Access()
        self.access.data = [User(1, 1, "Андрей"), User(1, 2, "Петр"), User(2, 3, "Василий"), User(3, 4, "Артур"),
                            User(3, 5, "Степан")]

    def test_read_json(self):
        self.assertEqual(self.access.read_json('data.json'),
                         {'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'}, '3': {'4': 'Артур', '5': 'Степан'}})

    def test_parse_data(self):
        self.assertEqual(self.access.parse_data({'1': {'1': 'Андрей', '2': 'Петр'}, '2': {'3': 'Василий'},
                                                 '3': {'4': 'Артур', '5': 'Степан'}}), [User(1, 1, "Андрей"),
                                                                                        User(1, 2, "Петр"),
                                                                                        User(2, 3, "Василий"),
                                                                                        User(3, 4, "Артур"),
                                                                                        User(3, 5, "Степан")])

    def test_compare_users(self):
        u1 = User(1, 1, "Виталий")
        u2 = User(2, 1, "Виталий")
        self.assertEqual(u1 == u2, True)

    def test_level_error(self):
        with self.assertRaises(LevelError):
            self.access.enter_system(User(5, 5, "Админ"), 5, "Степан")

    def test_access_error(self):
        with self.assertRaises(AccessError):
            self.access.enter_system(User(3, 5, "Админ"), 3, "Иван")


if __name__ == '__main__':
    # access = Access()
    # data = access.read_json('data.json')
    # print(data)
    # print(*access.parse_data(data))

    # print(*access.data)
    # print(access.enter_system(User(5, 5, 'Админ'), 4, "Артур"))
    doctest.testmod(verbose=True)
    pytest.main(['-v'])
    unittest.main(verbosity=True)
    doctest.testmod(verbose=True)
