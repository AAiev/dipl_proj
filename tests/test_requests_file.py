import pytest
from bs4 import BeautifulSoup

from constants import *
from src.requests_file import get_soup


@pytest.fixture
def params():
    params = PARAMS
    params['p'] = 500
    return params


@pytest.fixture
def params2():
    params2 = PARAMS
    params2['p'] = 1
    return params2


@pytest.fixture
def link():
    return URL_PARSING + '123'


@pytest.fixture
def link2():
    return URL_PARSING


def test_get_soup(link, params):
    soup = get_soup(link, params)
    assert soup is not None
    assert soup == 404


def test_get_soup2(link2, params2):
    soup = get_soup(link2, params2)
    assert soup.__class__ == BeautifulSoup
