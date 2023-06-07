from pathlib import Path


def rename_files(count_nums: int, extension_start: str, extension_final: str,
                 name_min: int, name_max: int, name_final: Path = '') -> None:
    p = Path(Path().cwd())
    serial_number = int('1' + ('0' * (count_nums - 1)))
    try:
        for obj in p.iterdir():
            print(obj)
            full_name = str(obj).split('\\')[-1]
            file_name, file_extension = full_name.split('.')
            if file_extension == extension_start:
                Path(full_name).rename(
                    f'{_name_clipping(file_name, name_min, name_max)}{name_final}{serial_number}.{extension_final}')
                serial_number += 1
    except:
        print('Не во всех файлах в директории есть расширение')


def _name_clipping(current_name: str, name_min: int, name_max: int) -> str:
    return current_name[name_min:name_max]


def test_func():
    return int('1' + ('0' * 5))
