"""

lambda em Python

Uma função lambda é um função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha.

"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


lista_1 = sorted(lista, key=lambda lista: lista['nome'])
lista_2 = sorted(lista, key=lambda lista: lista['sobrenome'])

exibir(lista_1)
exibir(lista_2)
