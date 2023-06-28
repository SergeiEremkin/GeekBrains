# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def num_exc():
    while True:
        num = input('Введите целое или вещественное число')
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                print(f'Вы ввели неправильное значение: {e}\n Попробуйте снова!')
    return num


if __name__ == '__main__':
    print(type(num_exc()))
