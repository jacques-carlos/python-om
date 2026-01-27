# Exemplo do uso dos sets

letras = set()

while True:
    print('\n\nQual é a letra misteriosa?')
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'h' in letras:
        print('PARABÉNS! Você acertou!')
        break

    print('Letras tentadas:', end=' ')
    for letra in letras:
        print(letra, end=', ')
