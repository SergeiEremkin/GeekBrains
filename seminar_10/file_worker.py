from pathlib import Path
from random import randint, uniform, choice
from typing import TextIO


class FileWorker:
    _MIN_NUM = -1000
    _MAX_NUM = 1000
    _VOWELS = 'aeiouy'
    _CONSTANTS = 'bcdfghjklmnqrstvwxz'

    def feel_numbers(self, count: int, file_name: str | Path) -> None:
        '''
        Записывает файл с генерацией количества строк в формате пары чисел int и float с разделителем '|'
        :param count:
        :param file_name:
        :return:
        '''

        with open(file_name, 'a', encoding='utf-8') as f:
            for _ in range(count):
                f.write(f'{randint(self._MIN_NUM, self._MAX_NUM)}|{uniform(self._MIN_NUM, self._MAX_NUM)}\n')

    def gen_files(self, extension: str, min_len_name: int = 6, max_len_name: int = 30, min_len_byte: int = 256,
                  max_len_byte: int = 4096, count_files: int = 42) -> None:
        '''
        Записывает файл с указанным расширением и с именем, которое генерится из гласных и согласных букв,
        строки ненерятся в байтах, которые определяются рэндомно в диапазоне
        :param extension:
        :param min_len_name:
        :param max_len_name:
        :param min_len_byte:
        :param max_len_byte:
        :param count_files:
        :return:
        '''
        for _ in range(count_files):
            rad_string = ''.join(choice(self._VOWELS) if i % 3 == 0 else choice(self._CONSTANTS)
                                 for i in range(randint(min_len_name, max_len_name)))
            data = bytes(randint(0, 255) for _ in range(randint(min_len_byte, max_len_byte)))
            with open(f'{rad_string}.{extension}', 'wb') as f:
                f.write(data)

    def name_gen(self, count: int, str_len_min: int, str_len_max: int, file: Path) -> None:
        '''
        Метод записывает рэндомно генерящиеся строки с большой буквы в файл
        :param count:
        :param str_len_min:
        :param str_len_max:
        :param file:
        :return:
        '''
        with open(file, 'a', encoding='utf-8') as f_2:
            for _ in range(count):
                rad_string = ''.join(choice(self._VOWELS) if i % 3 == 0 else choice(self._CONSTANTS)
                                     for i in range(randint(str_len_min, str_len_max)))
                f_2.write(f'{rad_string.capitalize()}\n')

    def rename_files(self, count_nums: int, extension_start: str, extension_final: str,
                     name_min: int, name_max: int, name_final: Path = '') -> None:
        '''
        Программа меняет название файлов в директории, расширение и обрезает название согласно аргументам
        :param count_nums:
        :param extension_start:
        :param extension_final:
        :param name_min:
        :param name_max:
        :param name_final:
        :return:
        '''
        p = Path(Path().cwd())
        serial_number = int('1' + ('0' * (count_nums - 1)))
        try:
            for obj in p.iterdir():
                full_name = str(obj).split('\\')[-1]
                file_name, file_extension = full_name.split('.')
                if file_extension == extension_start:
                    Path(full_name).rename(
                        f'{self._name_clipping(file_name, name_min, name_max)}{name_final}{serial_number}.{extension_final}')
                    serial_number += 1
        except:
            print('Не во всех файлах в директории есть расширение')

    def _name_clipping(self, current_name: str, name_min: int, name_max: int) -> str:
        return current_name[name_min:name_max]

    def _read_or_begin(self, fd: TextIO) -> str:
        line = fd.readline()
        if not line:
            fd.seek(0)
            return self._read_or_begin(fd)
        return line[:-1]

    def two_files_in_one(self, numbers: Path, words: Path, result: Path) -> None:
        '''
        Метод записывает в файл слово в верхнем либо нижнем регистре в зависимости от результата умножения и округленный
        либо по модулю результат умножения
        :param numbers: принимает файл, созданный методом feel_numbers
        :param words: принимает файл, созданный методом name_gen
        :param result: название результирующего файла
        :return:
        '''
        with (open(numbers, 'r', encoding='utf-8') as f_num,
              open(words, 'r', encoding='utf-8') as f_word,
              open(result, 'w', encoding='utf-8') as f_res
              ):
            len_numbers = sum(1 for _ in f_num)
            len_word = sum(1 for _ in f_word)
            for _ in range(max(len_numbers, len_word)):
                num = self._read_or_begin(f_num)
                word = self._read_or_begin(f_word)
                num_a, num_b = num.split('|')
                mult = int(num_a) * float(num_b)
                if mult < 0:
                    f_res.write(f'{word.lower()} {abs(mult)}\n')
                elif mult > 0:
                    f_res.write(f'{word.upper()} {round(mult)}\n')


if __name__ == '__main__':
    file_worker = FileWorker()
    #file_worker.feel_numbers(3, 'feel_numbers.txt')
    # file_worker.gen_files('bin', 5, 10, 1024, 4096, 5)
    #file_worker.name_gen(10, 4, 7, Path('name_gen.txt'))
    #file_worker.rename_files(5, 'bin', 'txt', 2, 4, 'rename_files')
    file_worker.two_files_in_one('feel_numbers.txt', 'name_gen.txt', 'result.txt')

