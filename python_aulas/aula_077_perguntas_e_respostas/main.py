# Exercício - Sistema de Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': ('4', 'c')
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': ('25', 'a')
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': ('5', 'b')
    },
    {
        'Pergunta': 'Quem é o maior time do Brasil?',
        'Opções': ['Santos', 'Corinthians', 'Palmeiras', 'São Paulo'],
        'Resposta': ('Palmeiras', 'c')
    }
]

letras = ['a', 'b', 'c', 'd']

while True:
    acertos = 0

    for pergunta in perguntas:
        print()
        print(pergunta['Pergunta'])
        print()

        for letra, alternativa in enumerate(pergunta['Opções']):
            print(f'{letras[letra]}) {alternativa}')
        print()
        resposta = input('Qual é a alternativa correta? ')

        if resposta in pergunta['Resposta']:
            print('Você acertou!')
            acertos += 1
        else:
            print('Você errou!')

    print()
    print('Acabaram as perguntas. Obrigado por jogar!')
    print(f'Você acertou {acertos} perguntas.')
    break
