from create_json import create_json
from pathlib import Path
from add_name_to_json import ui, read_json
from save_file_info import get_dirs_json, write_json, write_csv, write_pickle
if __name__ == '__main__':
    # create_json(Path('../work_with_files_pack/result.txt'))
    # ui()
    # print(type(read_json()))
    dict_json = get_dirs_json('C:\\Users\\Сергей\\PycharmProjects\\GeekBrains\\seminar_8')
    write_json('dir_info_json.json', dict_json)
    write_csv('dir_info_csv.csv', dict_json)
    write_pickle('dir_info_picle.pickle', dict_json)