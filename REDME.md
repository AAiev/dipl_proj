## Проект Веб скрапинг информации о товарах

### Описание

Есть сайт со списком товаров, рейтингом, условиями его применения и прочей информацией, которая помогает пользователю сделать выбор при покупке.
Необходимо произвести парсинг сайта для нового проект онлайн-магазина, которому нужно определить, какие товары имеют для пользователя наибольшую ценность по совокупности параметров, чтобы:

- закупить эти товары для продажи
- активно продвигать их в рекламе и получать прибыль


### Задача

создать CSV файл со всеми товарами магазина: `https://goldapple.ru/parfjumerija`

В этом файле должна быть следующая информация в текстовом формате:

1. ссылка на продукт
2. наименование
3. цена
4. рейтинг пользователей
5. описание продукта
6. инструкция по применению
7. страна-производитель

### При реализации проекта были исользованы:
* библиотеки requests и BeautifulSoup
* регулярные выражения
* CBV/FBV

### В папку `results` выложены полученные файлы:
* `products_links.csv` - файл с ссылками на все товары магазина
* `products_result.csv` - файл с информацией по товарам