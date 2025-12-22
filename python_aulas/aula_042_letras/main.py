# EXERCÍCIO

FRASE = 'O Python é uma linguagem de programação multiparadigma. '\
        'O Python foi criado por Guido van Rossum.'

tamanho_frase = len(FRASE)
i = 0
maior_quantidade = 0
letra_mais_frequente = ''

while i < tamanho_frase:
    letra_atual = FRASE[i]  # letra que está sendo analisada nessa iteração

    if letra_atual == ' ':  # pular caso seja espaço
        i += 1
        continue

    quantidade_atual = FRASE.count(letra_atual)

    if quantidade_atual > maior_quantidade:
        letra_mais_frequente = letra_atual
        maior_quantidade = quantidade_atual

    i += 1

print('A letra que mais apareceu foi '
      f'"{letra_mais_frequente}" com '
      f'{maior_quantidade} aparições.')
