import pytest

from src.product import Product
from src.requests_file import get_info_product


@pytest.fixture()
def test_link():
    test_link = link = 'https://goldapple.ru/review/product/19000220507'
    return test_link


@pytest.fixture()
def test_soup():
    return get_info_product('https://goldapple.ru/19000220507-vieri')


@pytest.fixture()
def test_product(test_soup):
    return Product(soup=test_soup, link='https://goldapple.ru/review/product/19000220507')


def test_init(test_soup, test_link, test_product):
    assert test_product.soup == test_soup
    assert test_product.link == 'https://goldapple.ru/review/product/19000220507'
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


def test_get_info(test_soup, test_link, test_product):
    test_info_dict = {'country_of_origin': 'США',
                      'description': 'Коллекция soulmate воплощает силу и единство пешек, '
                                     'коллективную уверенность и стремление поддерживать друг '
                                     'друга. По характеру пешка — решительная, амбициозная и '
                                     'бесстрашная фигура. Каждый аромат продуман, чтобы вы могли '
                                     'носить его самостоятельно или наслаивать с другими, создавая '
                                     'неповторимую композицию. Дизайн флаконов изящен, современен и '
                                     'сдержан — тонкие детали намекают на защитный слой брони. '
                                     'Разожгите страсть и откройте в себе лучшее с soulmate. Vieri '
                                     'перенесет вас в захватывающий дух пейзаж средиземноморья, где '
                                     'зародилась итальянская легенда о любви и дуэли на шахматах. '
                                     'Аромат начинается с нот красного лемонграсса, бодрящего '
                                     'лимона и шипучего розового перца. По мере развития аромата '
                                     'цветочные ноты пышного пиона и камелии проявляются на фоне '
                                     'соблазнительного мускуса, мистического ладана и насыщенной '
                                     'древесной амбры. Позвольте vieri очаровать вас пленительными '
                                     'первыми впечатлениями, которые выдерживают испытание '
                                     'временем.',
                      'id_prod': '19000220507',
                      'link': 'https://goldapple.ru/review/product/19000220507',
                      'manual': 'Распылите на кожу с расстояния 20-30 см.',
                      'name_brand': 'Mind Games',
                      'name_group': 'Парфюмерный экстракт',
                      'name_product': 'VIERI',
                      'price': {'price_old': 23220, 'price_sale': 16254}}
    info_list = test_product.get_info()
    assert type(info_list) is dict
    assert info_list == test_info_dict

    test_info_dict2 = {'country_of_origin': 'Нет данных',
                      'description': 'Аромат Mon Guerlain – гимн современной женственности. Он посвящается сильной, '
                                     'свободной и чувственной женщине, образ которой воплощает Анджелина Джоли.С 1828 '
                                     'года Дом Guerlain олицетворяет историю парфюмерии. Он изобретает новые смелые '
                                     'аккорды, создав за это время более 1 100 ароматов. Сегодня Тьерри Вассер является'
                                     ' пятым парфюмером Guerlain. Его новое творение Mon Guerlain – это восточный '
                                     'свежий аромат. Свежесть ЛАВАНДЫ КАРЛА, особая разновидность которой '
                                     'культивируется в Провансе, контрастирует с негой индийского ЖАСМИНА САМБАК и '
                                     'БЕЛОГО САНДАЛА из Австралии в сочетании с чувственной ТАИТЯНСКОЙ ВАНИЛЬЮ из '
                                     'Папуа-Новой Гвинеи.Парфюмерная вода Mon Guerlain представлена в легендарном '
                                     'флаконе-"четырехлистнике", созданном в 1908 году. Его чистый и графичный дизайн '
                                     'навеян очертаниями колбы алхимика, а своим названием он обязан пробочке, '
                                     'изготовленной из цельного куска материала и по форме напоминающей четырехлистник.',
                      'id_prod': '7753700002',
                      'link': 'https://goldapple.ru/review/product/7753700002',
                      'manual': 'нет данных',
                      'name_brand': 'Guerlain',
                      'name_group': 'Парфюмерная вода',
                      'name_product': 'Mon Guerlain',
                      'price': {'price_old': None, 'price_sale': 17120}}
    test_link2 = link = 'https://goldapple.ru/7753700002-mon-guerlain'
    test_link2_full = 'https://goldapple.ru/review/product/7753700002'
    test_soup2 = get_info_product(test_link2)
    test_product2 = Product(soup=test_soup2, link=test_link2_full)
    info_list2 = test_product2.get_info()
    assert type(info_list2) is dict
    assert info_list2 == test_info_dict2
