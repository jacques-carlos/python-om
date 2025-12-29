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
import pygame
from time import sleep


def linha():
    print('=' * 50)


def espaco():
    print()


# ==========================================================================
pygame.init()

som_acerto = pygame.mixer.Sound(
    'python_aulas/aula_047_palavra_secreta/som_acerto.mp3')
som_erro = pygame.mixer.Sound(
    'python_aulas/aula_047_palavra_secreta/som_erro.mp3')
som_final = pygame.mixer.Sound(
    'python_aulas/aula_047_palavra_secreta/som_final.mp3')

pygame.mixer.music.load('python_aulas/aula_047_palavra_secreta/music.mp3')
pygame.mixer.music.play(-1)
input()
pygame.event.wait()
# ==========================================================================

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
            som_final.play()
            linha()
            print('\033[1;34;40mVOCÊ GANHOU PARABÉNS!!\033[m'.center(62))
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
                pygame.quit()
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
            erro = 'ERRO! Digite apenas uma letra.'.center(50)
            print(f'\033[31m{erro}\033[m')
            continue

        # retorna erro caso o usuário não digite uma letra
        if not letra_digitada.isalpha():
            linha()
            erro = 'ERRO! Digite uma letra.'.center(50)
            print(f'\033[31m{erro}\033[m')
            continue

        # retorna erro caso o usuário já tenha digitado essa letra antes
        if letra_digitada in letras_tentadas:
            linha()
            erro = 'ERRO! Você já tentou essa letra.'.center(50)
            print(f'\033[31m{erro}\033[m')
            continue
        # adicina a letra digitada na lista de tentativas
        else:
            letras_tentadas.append(letra_digitada)

        # caso não ocorra nenhum erro, a resposta do usuário contará como uma tentativa
        tentativas += 1

        # caso o usuário acerte
        if letra_digitada in PALAVRA_SECRETA:
            linha()
            som_acerto.play()
            print('\033[1;32;40mVOCÊ ACERTOU!\033[m'.center(62))
            letras_acertadas.append(letra_digitada)
        # caso o usuário erre
        else:
            linha()
            som_erro.play()
            print(f'\033[1;31;40mVOCÊ ERROU!\033[m'.center(62))
