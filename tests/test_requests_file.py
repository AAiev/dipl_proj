import os.path

import pytest

from src.requests_file import get_all_product_links, get_info_product, get_rating_from_request


@pytest.fixture
def link_true(): # имя фикстуры любое
    return 'https://goldapple.ru/parfjumerija'

@pytest.fixture
def link_false():
    return 'https://goldapple.ru/parfjume'

@pytest.fixture
def link_product():
    return 'https://goldapple.ru/19000220507-vieri'

@pytest.fixture
def file_name_csv():
    return None

def test_get_all_product_links(link_true, link_false, file_name_csv):
    assert get_all_product_links(url=link_true, file_name_csv=file_name_csv) is None
    assert get_all_product_links(url=link_false, file_name_csv=file_name_csv) is None


def test_get_info_product(link_true, link_false):
    assert get_info_product(link=link_false) is None
