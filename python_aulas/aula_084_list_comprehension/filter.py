# filtro | filter

import pprint


def pp(item):
    pprint.pprint(item, sort_dicts=False, width=50)


numbers = [n for n in range(10) if n < 5]
print(numbers)
print()

####################################################################

products = [
    {'name': 'product_1', 'price': 20},
    {'name': 'product_2', 'price': 10},
    {'name': 'product_3', 'price': 30},
]

filter_products = [
    {**product, 'price': product['price'] * 0.9}  # desconto de 10%
    if product['price'] > 20 else {**product}  # para produtos > 20
    for product in products
    if product['price'] > 10
]

pp(filter_products)
