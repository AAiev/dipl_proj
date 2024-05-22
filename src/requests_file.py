import requests
from bs4 import BeautifulSoup


def get_soup(url: str, params: dict):
    """
    Данная функция из запрашиваемого УРЛа выдает ыщгз (отформатированный HTML) код для дальнейшей работы
    """
    resp = requests.get(url=url, params=params)
    if resp.status_code == 200:  # проверка статус-кода
        soup = BeautifulSoup(resp.content, 'html.parser')
    else:
        soup = resp.status_code
    return soup
