# Shallow Copy, Deep Copy e Atribuição simples

import copy

###########################################################

dicionario_1 = {
    'chave_1': 1,
    'chave_2': 2
}

# Atribuição Simples
dicionario_2 = dicionario_1  # Os dicionários apontam para o mesmo endereço na memória

dicionario_2['chave_2'] = 'Alterado em todos os dicionários'

print(dicionario_1)

###########################################################

dicionario_a = {
    'chave_a': 'a',
    'chave_b': 'b',
    'chave_c': [1, 2, 3]
}

# Shallow Copy - Cópia Rasa
dicionario_b = dicionario_a.copy()  # ou dicionario_b = copy.copy(dicionario_a)

# Deep Copy
dicionario_c = copy.deepcopy(dicionario_a)

dicionario_a['chave_a'] = 'alterei apenas aqui'
dicionario_a['chave_c'].append(4)

print(dicionario_a)
print(dicionario_b)
print(dicionario_c)
