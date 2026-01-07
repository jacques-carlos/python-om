# EXERCÍCIO

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você  vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.

"""
import os
from time import sleep


def linha():
    print('=' * 50)


def espaco():
    print()


PALAVRA_SECRETA = 'abacaxi'
tamanho_palavra_secreta = len(PALAVRA_SECRETA)

while True:
    tentativas = 0
    letras_tentadas = list()
    letras_acertadas = list()

    # título
    os.system('cls')
    linha()
    print('Adivinhe qual é a palavra secreta: '.upper().center(50))

    while True:
        # a medida que o usuário for acertado as letras, a resposta surgirá
        resposta = ''

        # formação da resposta
        for letra in PALAVRA_SECRETA:
            if letra in letras_acertadas:
                resposta += letra
            else:
                resposta += '*'

        # caso o usuário ganhe o jogo
        if resposta == PALAVRA_SECRETA:
            os.system('cls')
            linha()
            print('VOCÊ GANHOU PARABÉNS!!'.center(50))
            espaco()
            print(f'A palavra era: {PALAVRA_SECRETA}'.center(50))
            espaco()
            print(f'Tentativas: {tentativas}'.center(50))
            linha()
            espaco()

            jogar_novamente = input(
                'Deseja jogar novamente? Digite "S" para sim: ').strip().upper()
            if jogar_novamente.startswith('S'):
                break
            else:
                os.system('cls')
                print('Obrigador por jogar!'.center(50))
                exit()

        espaco()
        print(f'Resposta: {resposta}'.upper().center(50))
        espaco()
        print(f'Tentativas: {tentativas}'.center(50))
        linha()
        espaco()

        # o usuário digita uma letra
        letra_digitada = input('Digite uma letra: ').lower()

        # limpa o terminal
        os.system('cls')

        # retorna erro caso o usuário digite mais de uma letra
        if len(letra_digitada) > 1:
            linha()
            print('ERRO! Digite apenas uma letra.'.center(50))
            continue

        # retorna erro caso o usuário não digite uma letra
        if not letra_digitada.isalpha():
            linha()
            print('ERRO! Digite uma letra.'.center(50))
            continue

        # retorna erro caso o usuário já tenha digitado essa letra antes
        if letra_digitada in letras_tentadas:
            linha()
            print('ERRO! Você já tentou essa letra.'.center(50))
            continue
        # caso não: adicina a letra digitada na lista de tentativas
        else:
            letras_tentadas.append(letra_digitada)

        # caso não ocorra nenhum erro, a resposta do usuário contará como uma tentativa
        tentativas += 1

        # caso o usuário acerte
        if letra_digitada in PALAVRA_SECRETA:
            linha()
            print('VOCÊ ACERTOU!'.center(50))
            letras_acertadas.append(letra_digitada)
        # caso o usuário erre
        else:
            linha()
            print(f'VOCÊ ERROU!'.center(50))
