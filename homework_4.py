# Решить задачи, которые не успели решить на семинаре.

# в файле seminar_4.py дорешал все задачи


# Напишите функцию для транспонирования матрицы

def transparent_matrix(*a_list: list[[int]]) -> list[()] | str:
    is_transparent = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transparent = False
    if is_transparent:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(transparent_matrix([1, 3, 5], [2, 4, 6]))


# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Jack', cat={'Leopold': 2, 'Murka': 3}, turtle=['bill', 'jack', 'anatoliy'],
                     hamster={'edward', 'homa'}))


# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

#Доделал в файле seminar_2.py. Сохранил операции в словарь для большей информативности. Не судите строго.)
