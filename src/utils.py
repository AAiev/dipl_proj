import csv


def read_csv_file(file_name: str):
    with open(file_name, encoding='utf-8') as file_r:
        reader_object = csv.reader(file_r, delimiter=';')
        return reader_object


def create_csv_file(file_name: str, data=None):
    with open(file_name, mode='w', encoding='utf-8') as file_w:
        writer = csv.writer(file_w, delimiter=';')
        if data is not None:
            if data is list[list]:
                writer.writerows(data)
            else:
                writer.writerow(data)


def add_new_data_in_csv_file(file_name: str, data=None):
    with open(file_name, mode='a', encoding='utf-8') as file_a:
        writer = csv.writer(file_a, delimiter=';')
        if data is list[list]:
            writer.writerows(data)
        else:
            writer.writerow(data)
