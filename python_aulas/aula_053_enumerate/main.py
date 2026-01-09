"""

enumerate - enumera iteráveis (índices)

"""

lista = ['Maria', 'Helena', 'Luiz', 'João']

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

# Typer Conversion para lista:
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

# Maneira mais complexa (e mais usual):
for indice, item in enumerate(lista):
    print(indice, item)
