def format_price(price):
    return 'Цена ' + str(int(price)) + ' рублей.'


price1 = 56.24
display_price = format_price(price1)

print(display_price)