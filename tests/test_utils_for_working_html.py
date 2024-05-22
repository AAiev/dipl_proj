import pytest
from bs4 import BeautifulSoup

from src.requests_file import get_soup
from src.utils_for_working_html import get_links_products


@pytest.fixture
def soup():
    soup = get_soup('https://goldapple.ru/parfjumerija', {'p': 1})
    return soup

def test_get_links_products(soup):
    list_links_products = get_links_products(soup)

    assert len(list_links_products) == 24


