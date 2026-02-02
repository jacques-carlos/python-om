# dictionary comprehension

# dicionário a partir de um dicionário

products = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office'
}

new_products = {
    key: value.upper()
    # pode utilizar tupla para especificar mais de um tipo de instância ex:(int, float)
    if isinstance(value, str) else value
    for key, value in products.items()
}

print(new_products)


######################################################


# dicionário a partir de uma lista com tuplas

names = [
    ('mother', 'Joana'),
    ('father', 'Jonas'),
    ('son', 'João'),
    ('daughter', 'Jurema')

]

new_names = {
    key: value
    for key, value in names
}

old_names = dict(names)  # type conversion

print(new_names)
print(old_names)
