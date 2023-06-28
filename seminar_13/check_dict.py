# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_default(data: dict, key: int | str, value: int | str = 1):
    try:
        result = data[key]
    except KeyError as e:
        result = value
    return result


if __name__ == '__main__':
    print(get_default({1: '1', 2: '2', 3: '3'}, 4))
