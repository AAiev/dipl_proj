import pytest

from constants import PARAMS
from src.product import Product
from src.requests_file import get_soup


@pytest.fixture
def test_link():
    return 'https://goldapple.ru/review/product/19000225957'


@pytest.fixture
def test_soup():
    return get_soup('https://goldapple.ru/19000225957-dacha', params=PARAMS)


@pytest.fixture
def test_product(test_soup, test_link):
    return Product(soup=test_soup, link=test_link)


@pytest.fixture
def info_list(test_soup, test_link):
    test_product2 = Product(soup=test_soup, link=test_link)
    test_product2.name_group()
    test_product2.name_brand()
    test_product2.name_product()
    test_product2.get_price_old()
    test_product2.get_price_sale()
    test_product2.get_other_info()
    soup_rating = get_soup(test_link, params=PARAMS)
    test_product2.get_rating(soup_rating)
    info_list = test_product2.get_info_list()
    return info_list


def test_init(test_soup, test_link, test_product):
    assert test_product.soup == test_soup
    assert test_product.link == 'https://goldapple.ru/review/product/19000225957'
    assert test_product.name_group is None
    assert test_product.name_brand is None
    assert test_product.name_product is None
    assert test_product.price_sale is None
    assert test_product.price_old is None
    assert test_product.id_prod is None
    assert test_product.description is None
    assert test_product.country_of_origin is None
    assert test_product.manual is None
    assert test_product.rating is None
    assert type(test_product.info_list) is dict


def test_get_name_group(test_product):
    test_product.get_name_group()
    assert test_product.name_group == 'Парфюмерная вода'


def test_get_name_brand(test_product):
    test_product.get_name_brand()
    assert test_product.name_brand == 'Alfred ritchy'


def test_get_name_product(test_product):
    test_product.get_name_product()
    assert test_product.name_product == 'Dacha'


def test_get_price_sale(test_product):
    test_product.get_price_sale()
    assert test_product.price_sale == 10388


def test_get_price_old(test_product):
    test_product.get_price_old()
    assert test_product.price_old == 14840


def test_get_other_info(test_product):
    test_product.get_other_info()
    assert test_product.description == ('Бренд ALFRED RITCHY — путешествие по миру и запечатленные моменты через'
                                        ' ароматы с превосходными материалами и уникальными сочетаниями.Время 17:32'
                                        ' — безупречная ясность и спокойствие. Восточная, фруктовая и древесная '
                                        'парфюмерная вода DACHA посвящена даче, маленькому замку вдали от городского '
                                        'шума.')
    assert test_product.manual == 'Нанесите на кожу на расстоянии 20-30 см.'


# def test_get_rating(info_list):
#     assert info_list['rating'] == '4.5'
#
#
# def test_get_info_list(test_product2):
#     format_list_for_result_file = test_product2.get_format_list_for_result_file()
#     assert format_list_for_result_file == ['https://goldapple.ru/19000225957-dacha',
# #                                            'Парфюмерная вода', 'Alfred ritchy', 'Dacha', 10388, '4.5',
#                                            "Бренд ALFRED RITCHY — путешествие по миру и запечатленные моменты через "
#                                            "ароматы с превосходными материалами и уникальными сочетаниями.Время 17:32"
#                                            " — безупречная ясность и спокойствие. Восточная, фруктовая и древесная "
#                                            "парфюмерная вода DACHA посвящена даче, маленькому замку вдали от "
#                                            "городского шума.", 'Нанесите на кожу на расстоянии 20-30 см.', 'Франция'
#                                            ]
