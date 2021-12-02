# модуль призначено для роботи з зовнішніми файлами
# читання та виведення для вызуального контролю

# читання файла markets
def get_price():
    """читання файла 'markets'
    та формування списку цін
    повертає список цін
    """

    # накопичення даних файлу у списку
    with open("./data/markets.csv", 'r') as f:
        prices = f.readlines()

    # підготовка даних для подальшої обробки
        prices_splitted = []
    # порізати в циклі строки на окремі елементи
        for price in prices:
            obj = split_line(price)
            obj[0] = int(obj[0])
            prices_splitted.append(obj)

    return prices_splitted 


def split_line(line):
    """ повертає список об'єктів з строки"""
    object = line.split(',')     
    return object


# читання файла goods
def get_group():
    """читання файла 'goods'
    та формування списку товарних груп 
    повертає список товарних груп
    """
    #накопичення даних файлу у списку
    with open("./data/goods.csv", 'r') as f:
        groups = f.readlines()

    # підготовка даних для подальшої обробки
        groups_splitted = []
    # порізати в циклі строки на окремі елементи
        for group in groups:
            obj = split_line(group)
            obj[0] = int(obj[0])
            groups_splitted.append(obj)

    return groups_splitted 


# вивід списку цін
def show_prices(prices):
    """виводить список клієнтів по заданому інтервалу кодів
    """
    # задати інтервал кодів
    price_code_from = int(input('З якого кода ціни? '))
    price_code_to = int(input('До якого кода ціни? '))


    # відбір списку цін 
    filtered_prices = []
    for price in prices:
        if price_code_from <= price[0] <= price_code_to:
            filtered_prices.append(price)

    if len(filtered_prices) == 0:
        print('В списку цін нема таких кодів')
        return


    # вивід списку
    print('СПИСОК ЦІН')
    for price in filtered_prices:
        print(f'код товарної групи: {price[0]:3}  план: {price[1]:20} очікуєме виконання: {price[2]:25} рік{price[3][:-1]:30}')

# вивід списку товарних груп
def show_groups(groups):
    """виводить список клієнтів по заданому інтервалу кодів
    """
    # задати інтервал кодів
    group_code_from = int(input('З якого кода товарної групи? '))
    group_code_to = int(input('До якого кода товарної групи? '))


    # відбір списку цін 
    filtered_groups = []
    for group in groups:
        if group_code_from <= group[0] <= group_code_to:
            filtered_groups.append(group)

    if len(filtered_groups) == 0:
        print('В списку цін нема таких кодів')
        return


    # вивід списку
    print('СПИСОК ЦІН')
    for group in filtered_groups:
        print(f'код товарної групи: {group[0]:3} найменування тов групи: {group[1]:20} торгова знижка: {group[2][:-1]:25}')

if __name__ == '__main__':
    prices = get_price()
    groups = get_group()

    show_prices(prices)
    show_groups(groups)
    
    pass
