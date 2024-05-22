
from constants import *

def get_links_products(soup):
    """
    Получаем из супа - ссылки на продукты и возвращием список этих ссылок
    """
    list_links_products = []
    script = soup.find_all('a', class_=HTML_CLASSES_ON_PRODUCT_LIST_PAGE)
    for script in script:
        link = 'https://goldapple.ru' + script.get('href')
        list_links_products.append(link)
    return list_links_products
