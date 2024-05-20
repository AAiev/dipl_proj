import os
import pytest

from src.utils import read_csv_file, add_new_line_in_csv_file, create_csv_file


@pytest.fixture
def input_file():
    return os.path.join('tests', 'test_file.csv')


@pytest.fixture
def input_file2():
    return os.path.join('test_file2.csv')


def test_read_csv_file(input_file):
    assert read_csv_file(input_file) == ['1,2\n', '3,4']
    assert read_csv_file(input_file) != ['1', '3,4']


def test_add_new_line_in_csv_file(input_file2):
    create_csv_file(input_file2)
    test_list_row = ['1,2']
    add_new_line_in_csv_file(input_file2, test_list_row)
    assert read_csv_file(input_file2) == ['"1,2"\n']

def test_add_new_line_in_csv_file2(input_file2):
    create_csv_file(input_file2, [1, 2])
    test_list_rows = [[3, 4], [5, 6]]
    add_new_line_in_csv_file(input_file2, test_list_rows)
    assert read_csv_file(input_file2) == ['1,2\n', '"[3, 4]","[5, 6]"\n']


