import requests
from bs4 import BeautifulSoup

from src.utils import *
from constants import *


def get_all_product_links(url: str, file_name_csv: str):
    """Функция постраничного получения ссылок на товары со страницы списка товаров и
     запись их в файл .csv """
    try:
        create_csv_file(file_name=file_name_csv)
        list_page_with_zero_links = []
        list_links = []
        count_links = 0
        page = 1
        attempt = 1
        while True:
            if attempt < 5:
                resp = requests.get(url=url, params={'p': page, 'verify': False})
                if resp.status_code == 200:  # проверка статус-кода
                    soup = BeautifulSoup(resp.content, 'html.parser')
                    script = soup.find_all('a', class_=HTML_CLASSES_ON_PRODUCT_LIST_PAGE)
                    for script in script:
                        links = 'https://goldapple.ru' + script.get('href')
                        list_links.append(links)
                    if len(list_links) != 0:
                        count_links += len(list_links)
                        print(f'{page} - {len(list_links)}. Всего: {count_links}. Попыток: {attempt}')
                        if list_links:
                            add_new_line_in_csv_file(file_name=file_name_csv, data=list_links)
                            print(list_links)
                        list_links.clear()
                        attempt = 1
                        page += 1
                        continue
                    else:
                        if attempt == 4:
                            list_page_with_zero_links.append(page)
                            create_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS_ERRORS)
                            add_new_line_in_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS_ERRORS,
                                                     data=list_page_with_zero_links)
                            list_page_with_zero_links.clear()
                            print(f'{page} - {len(list_links)}. Всего: {count_links}. Попыток: {attempt}')
                            attempt = 1
                            page += 1
                            continue
                        else:
                            attempt += 1
                            continue
                else:
                    break
        create_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS_ERRORS)
        add_new_line_in_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS_ERRORS, data=list_page_with_zero_links)
    except Exception as ex:
        print(ex)
