import pytest

from src.utils_for_csv import read_csv_file, add_new_line_in_csv_file, create_csv_file


@pytest.fixture
def input_file():
    return 'test_file.csv'


def test_read_csv_file(input_file):
    create_csv_file(input_file, data=['num1', 'num2'])
    assert read_csv_file(input_file) == ['num1,num2\n']

    test_list_row = ['1', '2']
    add_new_line_in_csv_file(file_name=input_file, data=test_list_row)
    assert read_csv_file(input_file) == ['num1,num2\n', '1,2\n']


def test_add_new_line_in_csv_file(input_file):
    create_csv_file(file_name=input_file, data=['letter1', 'letter2'])
    test_list_rows = [['a', 'b'], ['c', 'd']]
    add_new_line_in_csv_file(file_name=input_file, data=test_list_rows)
    assert read_csv_file(file_name=input_file) == ['letter1,letter2\n', 'a,b\n', 'c,d\n']
