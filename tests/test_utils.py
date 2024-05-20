import os
import pytest

from src.utils import read_csv_file


@pytest.fixture
def input_file():
    return os.path.join('tests', 'test_file.csv')


def test_read_csv_file(input_file):
    assert read_csv_file(input_file) == ['1,2\n', '3,4']
    assert read_csv_file(input_file) != ['1', '3,4']

