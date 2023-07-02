# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import string
import doctest


def remove_chars(text: str) -> str:
    '''
    text
    >>> remove_chars('dddddd dddd')
    'dddddd dddd'
    >>> remove_chars('AAA AA')
    'aaa aa'
    >>> remove_chars('a,a,n: v.v;')
    'aan vv'
    >>> remove_chars('БВАОПоаоваов')
    ''
    >>> remove_chars('WWW,3322,ГГ:')
    'www'
    '''
    alpha = string.ascii_letters + ' '
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    # print(remove_chars('sDDsdsd вывывывывы  выввы1323232'))
    doctest.testmod(verbose=True)
