person_name = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

person_data = {
    'idade': 16,
    'altura': 1.6
}

# extrair dados de um dicionário: **
person = {**person_name, **person_data, 'nome': 'Lúcia'}

print(person)
