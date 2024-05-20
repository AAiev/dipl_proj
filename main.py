import os
import time

from constants import *
from src.product import Product
from src.requests_file import get_all_product_links, get_info_product
from src.utils import read_csv_file, create_csv_file, add_new_line_in_csv_file


def main():
    # парсим ссылки всех товаров в CSV файл (FILE_CSV_WITH_LINKS_PRODUCTS)
    # get_all_product_links(URL_PARSING, FILE_CSV_WITH_LINKS_PRODUCTS)

    # создаем файл с результатами парсинга
    create_csv_file(file_name=FILE_CSV_WITH_RESULT, data=RESULT_FILE_HEADLINES)

    # читаем из файла построчно списки ссылок и получаем по каждой инфу.
    reader_object = read_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS)
    count_product = 0
    links_list = None
    for r in reader_object:
        if len(r) > 1:
            if ',' in r:
                links_list = r.strip().split(',')
            else:
                links_list = [r.strip()]
        for link in links_list:
            while True:
                soup = get_info_product(link)
                product = Product(soup, link)
                product.get_info()
                if product.info_list is None:
                    continue
                else:
                    product.get_rating_product()
                    product_info = product.get_format_list_for_result_file()
                    if os.path.exists(FILE_CSV_WITH_RESULT):
                        add_new_line_in_csv_file(file_name=FILE_CSV_WITH_RESULT, data=product_info)
                    else:
                        create_csv_file(file_name=FILE_CSV_WITH_RESULT, data=product_info)
                    count_product += 1
                    print(f'{count_product} - {product.id_prod}')
                    break


if __name__ == '__main__':
    main()
