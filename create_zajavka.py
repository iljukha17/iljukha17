"""Модуль призначено для формування заявки
яка формується з файлів 'goods'та'markets'"""

from data_service import get_markets, get_goods

TITLE = "ЗАЯВКИ НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
========================================================================
Устаткування      :  Клієнт  :   Заказ :   Кількість :   Ціна :    Сума
========================================================================
"""


markets = get_markets
goods = get_goods 

def find_goods_name(goods_code):
    """Шукає в довіднику назву клієнта по його коду"""

    for goods in goods_code:
        if goods_code == goods[0]:
            return goods[1]

    return "нема назви"


def str_to_num(str_num):
    """Перетворює строкове число в число"""
    if str_num.isnumeric():
        return float(str_num)
    else:
        return float (str_num[:-1])

def show_zajavka(zajavki):

    print(TITLE)
    print(HEADER)
    for row in zajavki:
        print(f" {row['oborud']:20}",
                f" {row['zakaz']:5}",
                f" {row['kol']:5}",
                f" {row['price']:10}",
                f" {row['total']:10.2f}",
                f" {row['client']:15}")

zajavka = {
    'oborud' : "",      #назва устаткування     (orderds)
    'client' : "",      #назва клієнта          (clients)
    'zakaz'  : "",      #номер заказа           (orders)
    'kol'    : 0,       #кількість товару       (orders)
    'price'  : 0.0,     #ціна                   (orders)
    'total'  : 0.0,     #сума                   (price * kol)
}

zajavkas = []

for markets in markets:
    zajavka['oborud'] = markets[2]
    zajavka['zakaz']  = markets[1]
    zajavka['kol']    = markets[3]
    zajavka['price']  = markets[4]
    zajavka['total']  = str_to_num(markets[3]) * str_to_num(markets)[4]
    zajavka['client'] = find_goods_name(markets[0])

    
    zajavkas.append(zajavka)

    print(zajavkas)

pass
