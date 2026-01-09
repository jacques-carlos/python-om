"""

split e join com strings e listas
split - divide uma str
join - une uma str
strip - corta os espaços
lstrip / rstrig

"""

# Unir essas palavras com hífen:
palavras = 'olha só que coisa interessante'

# Criação de uma lista
lista_palavras_original = palavras.split(' ')

print(lista_palavras_original)

# Em algumas situações, será necessário eliminar espaços excedentes (nessa não)
lista_palavras_formatada = []

for f in lista_palavras_original:
    lista_palavras_formatada.append(f.strip())
print(lista_palavras_formatada)

# União da lista para formar a nova string
palavras_unidas = '-'.join(lista_palavras_formatada)
print(palavras_unidas)
