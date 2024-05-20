# Файл с используемыми переменными

# сайт для парсинга
URL_PARSING = 'https://goldapple.ru/parfjumerija'
URL_PARSING_START_PAGE = 'https://goldapple.ru/'
URL_PARSING_INFO_PRODUCT_PREFIX = 'https://goldapple.ru/review/product/'

# классы стилей объектов-товаров на страницах списков товаров, которые парсим
HTML_CLASSES_ON_PRODUCT_LIST_PAGE = [
    '_9Bnes wEteb h92Dk rMYg4',
    'TjeQ6 _8l-0A Ks4bP VGaZJ',
    '_2uZNh _0wwKr Ol19w RWNxw',
]

HTML_CLASSES_ON_PRODUCT_INFO_PAGE = {
    'group': ['Ab0Ao'],
    'brand': ['_9Bnes wEteb h92Dk uEBTc', 'TjeQ6 _8l-0A Ks4bP geLVL'],
    'product': ['jOTnj', '_2k5cN'],
    'price_sale': ['_0OnLg +Ns2G', 'Kd+G7 CB1W3'],
    'price_old': ['_0OnLg ZIw21 M21En +Ns2G', 'Kd+G7 xx1gT oEjom CB1W3'],
    'info_product': ['TlDWb'],
    'id_and_country': ['Ytk5J']
}


# Название файла .csv со списком ссылок на все товары
FILE_CSV_WITH_LINKS_PRODUCTS = 'products_links.csv'
FILE_CSV_WITH_LINKS_PRODUCTS_ERRORS = 'zero_links'
FILE_CSV_WITH_RESULT = 'products_result.csv'
FILE_LINKS_WITH_ERROR = 'products_result_links_error.csv'
FILE_CSV_WITH_ERROR = ''

# Названия колонок итогового файла
RESULT_FILE_HEADLINES = ['ССЫЛКА НА ПРОДУКТ', 'ГРУППА',
                         'БРЕНД', 'НАИМЕНОВАНИЕ',
                         'ЦЕНА', 'РЕЙТИНГ ПОЛЬЗОВАТЕЛЕЙ',
                         'ОПИСАНИЕ ПРОДУКТА', 'ИНСТРУКЦИЯ ПО ПРИМЕНЕНИЮ',
                         'СТРАНА-ПРОИЗВОДИТЕЛЬ']

# Параметры для запроса
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'YaBrowser/23.1.1.1114 Yowser/2.5 Safari/537.36'
}
verify = False
PARAMS = {'headers': headers, 'verify': verify}
