"""

Iterando strings com while

"""

nome = input('Digite seu nome: ').lower()
tamanho_nome = len(nome)
# o índice é responsável por selecionar as letras
indice = letra = 0
nome_final = ''  # esse será o nome final entregue ao usuário

# seu nome sem as letras "a" e "u"
while indice < tamanho_nome:
    # variável que representa a letra que está sendo trabalhada
    letra = nome[indice]

    if letra == 'a' or letra == 'u':
        indice += 1
        continue
    else:
        nome_final += letra
        indice += 1

print(nome_final)
