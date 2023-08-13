"""
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os


def main(user_path):
    file_name = os.path.basename(user_path)
    path_to_file = os.path.dirname(user_path)
    file_extension = os.path.splitext(user_path)[1]
    return (path_to_file, file_name, file_extension)


if __name__ == '__main__':
    # path_from_user = input('Enter an absolute path to file: ')
    path_from_user = '/home/xumpocmb/Documents/GB/python/s5/task1.py'
    print(main(user_path=path_from_user))