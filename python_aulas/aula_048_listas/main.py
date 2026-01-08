"""

Listas em Python
Tipo List - Mutável
Suporta valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Operador de atribuição (=) para dados mutáveis: faz com que as variáveis apontem para o mesmo valor na memória  

Create Read Update  Delete (CRUD)
Criar  Ler  Alterar Apagar

"""


# Cada elemento em uma lista é um ITEM, que pode ser acessado pelos índices (positivos e negativos)
lista = [123, True, 'Luiz Otávio', 1.2, []]

lista[-3] = 'Maria José'
lista.append('James Rodriguez')

print(lista)
print(lista[2], type(lista[2]))


"""
ALGUNS MÉTODOS BÁSICOS

append    -> adiciona um item ao final da lista
insert    -> adiciona um item no índice escolhido
pop       -> retorna o item final da lista ou um item escolhido (removendo-o)
    ultimo_valor = lista.pop()
del       -> apaga um índice
clear     -> limpa a lista
extend    -> estende a lista      ex: lista_a.extend(lista_b)
+         -> cocatena listas      ex: lista_c = lista_a + lista_b
copy      -> Copia os dados de uma lista para outra
    lista_a = lista_b.copy()
"""
