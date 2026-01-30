# Empacotamento e Desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
print('a =', a)
print('b =', b)

person = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

# Pega a key
a, b = person
print(a, b)

# Pega o Value
a, b = person.values()
print(a, b)

# Pega tudo
(a1, a2), (b1, b2) = person.items()
print(a1, a2)
print(b1, b2)
