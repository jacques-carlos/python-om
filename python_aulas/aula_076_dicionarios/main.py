"""

Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos na lista
e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

"""

print('Maneira menos usual para criar dicionários')
pessoa = dict(nome='Jacques', sobrenome='Santos')
print(pessoa)

pessoa = {
    'nome': 'Jacques',
    'sobrenome': 'Santos',
    'idade': 20,
    'altura': 1.8,
    'endereços': [
        {'avenida': 'Morumbi', 'número': 500},
        {'avenida': 'Brasil', 'número': 1000},
        {'avenida': 'Futuro', 'número': 9999}
    ]
}
print(pessoa)
print(pessoa['endereços'][2])
for chave in pessoa:
    print(chave, pessoa[chave])
