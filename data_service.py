# модуль призначено для роботи з зовнішніми файлами
# читання та виведення для вызуального контролю

# читання файла markets
def get_markets():
    """читання файла 'markets'
    та формування списку цін
    повертає список цін
    """

    # накопичення даних файлу у списку
    with open("./data/markets.csv", 'r') as f:
        markets = f.readlines()

    # підготовка даних для подальшої обробки
        markets_splitted = []
    # порізати в циклі строки на окремі елементи
        for markets in markets:
            obj = split_line(markets)
            obj[0] = int(obj[0])
            markets_splitted.append(obj)

    return markets_splitted 


def split_line(line):
    """ повертає список об'єктів з строки"""
    object = line.split(',')     
    return object


# читання файла goods
def get_goods():
    """читання файла 'goods'
    та формування списку товарних груп 
    повертає список товарних груп
    """
    #накопичення даних файлу у списку
    with open("./data/goods.csv", 'r') as f:
        goods = f.readlines()

    # підготовка даних для подальшої обробки
        goods_splitted = []
    # порізати в циклі строки на окремі елементи
        for goods in goods:
            obj = split_line(goods)
            obj[0] = int(obj[0])
            goods_splitted.append(obj)

    return goods_splitted 


# вивід списку цін
def show_markets(markets):
    """виводить список клієнтів по заданому інтервалу кодів
    """
    # задати інтервал кодів
    markets_code_from = int(input('З якого кода ринкові ціни? '))
    markets_code_to = int(input('До якого кода ринкові ціни? '))


    # відбір списку цін 
    filtered_markets = []
    for markets in markets:
        if markets_code_from <= markets[0] <= markets_code_to:
            filtered_markets.append(markets)

    if len(filtered_markets) == 0:
        print('В списку ринкових цін нема таких кодів')
        return


    # вивід списку
    print('СПИСОК РИНКОВИХ ЦІН')
    for markets in filtered_markets:
        print(f'код товару: {markets[0]:3}  ринкові ціни на 2.11: {markets[1]:20} ринкові ціни на 10.11: {markets[1]:20} ринкові ціни на 14.11: {markets[1]:20} ринкові ціни на 24.11: {markets[1]:20} рік{markets[3][:-1]:30}')

# вивід списку товарних груп
def show_goods(goods):
    """виводить список товарів по заданому інтервалу кодів
    """
    # задати інтервал кодів
    goods_code_from = int(input('З якого кода довідника товарів? '))
    goods_code_to = int(input('До якого кода довідника товарів? '))


    # відбір списку цін 
    filtered_goods = []
    for goods in goods:
        if goods_code_from <= goods[0] <= goods_code_to:
            filtered_goods.append(goods)

    if len(filtered_goods) == 0:
        print('В списку товарів нема таких кодів')
        return


    # вивід списку
    print('СПИСОК ТОВАРІВ')
    for goods in filtered_goods:
        print(f'код товару: {goods[0]:3} найменування товару: {goods} од.виміру: {goods} роздрібна ціна: {goods[1]:20}')

if __name__ == '__main__':
    markets = get_markets()
    goods = get_goods()

    show_markets(markets)
    show_goods(goods)
    
    pass
