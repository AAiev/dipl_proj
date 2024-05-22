# файл с функциями для работы с .csv файлами
import csv


def read_csv_file(file_name):
    """
    функция чтения файла .csv
    возвращает reader_object
    """
    with open(file_name, encoding='utf-8') as r_file:
        data = r_file.readlines()
        return data


def create_csv_file(file_name: str, data=None):
    """ функция создания файла .csv"""
    with open(file_name, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator="\r")
        if data is not None:
            file_writer.writerow(data)


def add_new_line_in_csv_file(file_name: str, data=None):
    """ функция добавления записи (списка) в конец файла """
    with open(file_name, mode="a", encoding='utf-8') as a_file:
        file_writer = csv.writer(a_file, delimiter=',', lineterminator="\r")
        if data is list[list]:
            file_writer.writerows(data)
        else:
            file_writer.writerow(data)
