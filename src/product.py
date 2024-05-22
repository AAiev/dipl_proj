import re

from constants import *


class Product:
    def __init__(self, soup, link):
        self.soup = soup
        self.link = link
        self.name_group = None
        self.name_brand = None
        self.name_product = None
        self.price_sale = None
        self.price_old = None
        self.id_prod = None
        self.description = None
        self.country_of_origin = None
        self.manual = None
        self.rating = None
        self.info_list = {}

    def get_name_group(self):
        self.name_group = self.soup.find('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['group']).text.strip()

    def get_name_brand(self):
        if self.soup.find('a', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['brand']):
            self.name_brand = (self.soup.find('a', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['brand']).text
                               .strip())
        else:
            self.name_brand = (self.soup.find('span', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['brand'])
                               .text.strip())

    def get_name_product(self):
        self.name_product = (self.soup.find('span', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['product']).text.strip())

    def get_price_sale(self):
        if self.soup.find('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['price_sale']):
            price_sale_str = (self.soup.find('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['price_sale']).text
                              .strip().replace(' ', ''))
            self.price_sale = int(re.match(r'\d+', price_sale_str).group())
        else:
            self.price_sale = None

    def get_price_old(self):
        if self.soup.find('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['price_old']):
            price_old_str = (self.soup.find('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['price_old']).text
                             .strip().replace(' ', ''))
            self.price_old = int(re.match(r'\d+', price_old_str).group())
        else:
            self.price_old = None

    def get_other_info(self):
        info_prod = self.soup.find_all('div', class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['info_product'])
        self.id_prod = (
            info_prod[0].find(class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['id_and_country']).text.strip())
        if info_prod[0].find(itemprop='description'):
            self.description = info_prod[0].find(itemprop='description').text.replace('\n', '').strip()
        else:
            self.description = 'нет данных'
        if "ополнительная информация" in str(info_prod[-1]):
            if 'происхождения' in info_prod[-1].text and 'изготовитель' in info_prod[-1].text:
                self.country_of_origin = re.search(r'(?<=происхождения)([\w\s()]+)(?=изготовитель)',
                                                   info_prod[-1].text).group()
            elif 'происхождения' in info_prod[-1].text:
                self.country_of_origin = re.search(r'(?<=происхождения)\w+\s*\w+\s*\w+', info_prod[-1].text).group()
            else:
                self.country_of_origin = 'Нет данных'
        elif info_prod[-1].find(class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['id_and_country']):
            self.country_of_origin = info_prod[-1].find(
                class_=HTML_CLASSES_ON_PRODUCT_INFO_PAGE['id_and_country']).text.strip()
        else:
            self.country_of_origin = 'Нет данных'
        if len(info_prod) == 5:
            self.manual = info_prod[1].text.replace('\n', '').strip()
        else:
            if "применение" in str(info_prod[1]):
                self.manual = info_prod[1].text.replace('\n', '').strip()
            else:
                self.manual = 'нет данных'

    def get_rating(self, soup_rating):
        self.rating = soup_rating.find('div', itemprop='ratingValue').text.strip()
        self.info_list['rating'] = self.rating

    def get_info_list(self):
        info_list = {'id_prod': self.id_prod,
                     'link': self.link,
                     'name_group': self.name_group,
                     'name_brand': self.name_brand,
                     'name_product': self.name_product,
                     'price': {'price_sale': self.price_sale,
                               'price_old': self.price_old},
                     'description': self.description,
                     'manual': self.manual,
                     'country_of_origin': self.country_of_origin,
                     'rating': self.rating}
        return info_list

    def get_format_list_for_result_file(self):
        format_list_for_result_file = [
            self.link, self.name_group, self.name_brand, self.name_product, self.price_sale, self.rating,
            self.description, self.manual, self.country_of_origin
        ]
        return format_list_for_result_file
