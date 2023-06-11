# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json


def add_data(name: str, personal_id: int, level: int) -> dict[int, dict[str, int]]:
    return {level: {personal_id: name}}


def write_json(data: dict) -> None:
    file = 'data.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_json():
    with open("data.json", "r", encoding='utf-8') as read_file:
        # data = read_file.read()
        # if data:
        #     return {}
        data_from_file = json.load(read_file)
    return data_from_file


def make_base(data_to_write: dict):
    base_list = []
    read_data = read_json()
    base_list.append(read_data)
    return base_list


def ui():
    base_dict = read_json()
    exit_program = False
    print("Добро пожаловать в программу. Введите данные для создания файла...")
    while not exit_program:
        personal_id = int(input("Введите id: "))
        name = input("Введите имя: ")
        level = int(input("Введите уровень доступа: "))
        continue_program = input("Хотите продолжить? да/нет")
        if continue_program == 'нет':
            exit_program = True
        res_dict = (add_data(name, personal_id, level))
        if level in base_dict:
            base_dict[level].update({personal_id: name})
        else:
            base_dict[level] = {personal_id: name}
    write_json(base_dict)
