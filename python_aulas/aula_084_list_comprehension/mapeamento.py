# Mapeamento de dados em list comprehension

products = [
    {'name': 'product_1', 'price': 20},
    {'name': 'product_2', 'price': 10},
    {'name': 'product_3', 'price': 30},
]

news_products = [
    {'name': product['name'], 'price': product['price']
        * 0.9}  # desconto de 10%
    for product in products
]

# or

news_products_2 = [
    {**product, 'price': product['price'] * 0.9}  # desconto de 10%
    if product['price'] > 20 else {**product}  # para produtos > 20
    for product in products
]

print(*products, sep='\n')
print()
print(*news_products, sep='\n')
print()
print(*news_products_2, sep='\n')
