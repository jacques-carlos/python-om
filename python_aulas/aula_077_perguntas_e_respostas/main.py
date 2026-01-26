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
        'Pergunta': 'Quantas Copas do Mundo de Futebol tem o Brasil?',
        'Opções': ['1', '4', '5', '2'],
        'Resposta': ('5', 'c')
    }
]

letras = ['a', 'b', 'c', 'd']

while True:
    quantidade_acertos = 0
    quantidade_perguntas = 0  # utilizar a função len() ocasionaria futuras limitações

    for pergunta in perguntas:
        quantidade_perguntas += 1
        print(f'\n[PERGUNTA {quantidade_perguntas}] {pergunta['Pergunta']}')

        for indice, alternativa in enumerate(pergunta['Opções']):
            print(f'{letras[indice]}) {alternativa}')
        resposta = input('Qual é a alternativa correta? ')

        if resposta in pergunta['Resposta']:
            print('Você acertou!')
            quantidade_acertos += 1
        else:
            print('Você errou!')

    print('\nAcabaram as perguntas. Obrigado por jogar!')
    print(
        f'Você acertou {quantidade_acertos} de {quantidade_perguntas} perguntas.')
    break
