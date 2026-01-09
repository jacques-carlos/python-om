"""

Introdução ao desempacotamento

"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome1, nome2, nome3)

# Exibir primeiro nome
nome, *_ = ['Maria', 'Helena', 'Luiz']
print(f'Nome: {nome}, Resto: {_}')

# Exibir terceiro nome
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(f'Nome: {nome}, Resto: {_}')

# O underline serve como um "resto" nessas situações, uma variável que existe mas não tem uso
# Isso foi definido por uma convenção, não é uma regra oficial do Python
