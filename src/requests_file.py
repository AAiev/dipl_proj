import os

import requests
from bs4 import BeautifulSoup
import time

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
                            # print(list_links)
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


def get_info_product(link: str):
    """
    Функция получения 'супа' - html-кода страницы для последующего разбора
    """
    attempt = 1
    soup = None
    while True:
        if attempt < 5:
            try:
                resp = requests.get(url=link, params=PARAMS)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.content, 'html.parser')
                    break
                else:
                    if attempt < 3:
                        attempt += 1
                        continue
                    elif attempt == 3:
                        attempt += 1
                        time.sleep(3)
                        continue
                    else:
                        if os.path.exists(FILE_LINKS_WITH_ERROR):
                            add_new_line_in_csv_file(file_name=FILE_LINKS_WITH_ERROR, data=[link])
                            attempt = 1
                            break
                        else:
                            create_csv_file(file_name=FILE_LINKS_WITH_ERROR, data=[link])
                            attempt = 1
                            break
            except Exception as ex:
                if attempt < 3:
                    attempt += 1
                    continue
                elif attempt == 3:
                    attempt += 1
                    time.sleep(2)
                    continue
                else:
                    if os.path.exists(FILE_LINKS_WITH_ERROR):
                        add_new_line_in_csv_file(file_name=FILE_LINKS_WITH_ERROR, data=[link])
                        attempt = 1
                        time.sleep(2)
                        break
                    else:
                        create_csv_file(file_name=FILE_LINKS_WITH_ERROR, data=[link])
                        attempt = 1
                        time.sleep(2)
                        break
    return soup


def get_rating_from_request(url):
    while True:
        try:
            resp = requests.get(url=url, params=PARAMS)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                rating = soup.find('div', itemprop='ratingValue').text.strip()
                break
            else:
                raise Exception
        except Exception as e:
            print(e)
            time.sleep(3)
            continue
    return rating
