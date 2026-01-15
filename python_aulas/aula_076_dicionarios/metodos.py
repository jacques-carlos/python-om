"""

Métodos úteis dos dicionários em Python (em funções)

len - quantidade de chaves
keys - iterável com as chaves
values - iterável com valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (Shallow Copy)
get - obtém uma chave
pop - apaga e retorna um item especificado
popitem - apaga o último item adicionado
update - atualiza um dicionário

"""

pessoa = {
    'nome': 'Jacques',
    'sobrenome': 'Santos',
    'idade': 20,
    'sexo': 'masculino'
}

# print(len(pessoa))  # len

# print(list(pessoa.items()))  # keys, values, items

# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('sexo', 'não identificado')  # setdefault

# print(pessoa.get('nome'))  # get
# print(pessoa.get('endereço'))  # get

# idade = pessoa.pop('idade')  # pop
# print(idade)
# print(pessoa)

# ultima_chave = pessoa.popitem()  # popitem
# print(ultima_chave)
# print(pessoa)

# update
pessoa.update({
    'nome': 'Carlos',
    'idade': 20
})
print(pessoa)

pessoa.update(nome='Jacques', sobrenome='Filho')
print(pessoa)

tupla = (('idade', 21), ('país', 'Brasil'))
pessoa.update(tupla)
print(pessoa)

pessoa.update([('país', 'Canadá'), ('idade', 25)])
print(pessoa)
