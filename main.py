from constants import *
from src.product import Product
from src.requests_file import get_soup
from src.utils_for_csv import create_csv_file, add_new_line_in_csv_file, read_csv_file
from src.utils_for_working_html import get_links_products



def main():
    def parsing_links_to_file():
        create_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS)
        params = PARAMS
        page = 1
        count_links = 0
        while True:
            params['p'] = page
            try:
                # получаем "СУП" (отформатированный HTML код) страницы с продуктами
                soup_all_products = get_soup(url=URL_PARSING, params=params)
                # получаем из "СУПа" ссылки на продукты и сохраняем в файл
                if soup_all_products != 404:
                    list_links_products = get_links_products(soup_all_products)
                    if len(list_links_products) != 0:
                        count_links += len(list_links_products)
                        print(f'{page} - {len(list_links_products)}. Всего: {count_links}.')
                        page += 1
                        add_new_line_in_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS, data=list_links_products)
                        continue
                    else:
                        continue
                else:
                    break
            except Exception as e:
                print(e)
                continue

    def parsing_info_about_products_from_file():
        # читаем из файла построчно списки ссылок и получаем по каждой инфу.
        reader_object_links = read_csv_file(file_name=FILE_CSV_WITH_LINKS_PRODUCTS)
        create_csv_file(file_name=FILE_CSV_WITH_RESULT, data=RESULT_FILE_HEADLINES)
        count_product = 0
        links_list = None
        for r in reader_object_links:
            if len(r) > 1:
                if ',' in r:
                    links_list = r.strip().split(',')
                else:
                    links_list = [r.strip()]
            for link in links_list:
                while True:
                    try:
                        soup = get_soup(url=link, params=PARAMS)
                        product = Product(soup, link)
                        product.get_name_group()
                        product.get_name_brand()
                        product.get_name_product()
                        product.get_price_old()
                        product.get_price_sale()
                        product.get_other_info()
                        soup_rating = get_soup(f"{URL_PARSING_INFO_PRODUCT_PREFIX}{product.id_prod}", params=PARAMS)
                        product.get_rating(soup_rating)
                        info_list = product.get_info_list()
                        if len(info_list) == 0:
                            continue
                        list_for_result_file = product.get_format_list_for_result_file()
                        count_product += 1
                        print(f"{count_product} - {product.id_prod}")
                        break
                    except Exception as e:
                        print(e)
                        continue
                add_new_line_in_csv_file(file_name=FILE_CSV_WITH_RESULT, data=list_for_result_file)

    user_input = input("1 - Запустить код полностью\n"
                       "2 - Запустить парсинг только ссылок на товары и запись их в файл\n"
                       "3 - Запустить парсинг информации товаров по ссылкам из файла\n")

    if int(user_input) == 1:
        parsing_links_to_file()
        parsing_info_about_products_from_file()
    elif int(user_input) == 2:
        parsing_links_to_file()
    elif int(user_input) == 3:
        parsing_info_about_products_from_file()
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()
