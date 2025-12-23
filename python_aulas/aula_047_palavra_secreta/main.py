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


PALAVRA_SECRETA = 'dinamarca'
tamanho_palavra_secreta = len(PALAVRA_SECRETA)

# título
linha()
print('Adivinhe qual é a palavra secreta: '.upper().center(50))
linha()
espaco()
sleep(2)

tentativas = 0
letras_tentadas = list()
letras_acertadas = list()

while True:
    # a media que o usuário for acertado as letras, a resposta surgirá
    resposta = ''

    # o usuário digita uma letra
    letra_digitada = input('Digite uma letra: ').lower()

    # limpa o terminal
    os.system('cls')

    # retorna erro caso o usuário digite mais de uma letra
    if len(letra_digitada) > 1:
        print('\033[31mERRO! Digite apenas uma letra.\033[m')
        continue

    # retorna erro caso o usuário não digite uma letra
    if not letra_digitada.isalpha():
        print('\033[31mERRO! Digite uma letra.\033[m')
        continue

    # retorna erro caso o usuário já tenha digitado essa letra antes
    if letra_digitada in letras_tentadas:
        print('\033[31mERRO! Você já tentou essa letra.\033[m')
        continue
    # adicina a letra digitada na lista de tentativas
    else:
        letras_tentadas.append(letra_digitada)

    # caso não ocorra nenhum erro, a resposta do usuário contará como uma tentativa
    tentativas += 1

    # caso o usuário acerte
    if letra_digitada in PALAVRA_SECRETA:
        espaco()
        linha()
        som_acerto.play()
        print('\033[1;32;40mVOCÊ ACERTOU!\033[m'.center(62))
        letras_acertadas.append(letra_digitada)
    # caso o usuário erre
    else:
        espaco()
        linha()
        som_erro.play()
        print(f'\033[1;31;40mVOCÊ ERROU!\033[m'.center(62))

    # formação da resposta
    for letra in PALAVRA_SECRETA:
        if letra in letras_acertadas:
            resposta += letra
        else:
            resposta += '*'

    espaco()
    print(f'Resposta: {resposta}'.upper().center(50))
    espaco()
    print(f'Tentativas: {tentativas}'.center(50))
    linha()
    espaco()
    sleep(2)

    # caso o usuário ganhe o jogo
    if resposta == PALAVRA_SECRETA:
        som_final.play()
        linha()
        print('\033[1;34;40mVOCÊ GANHOU PARABÉNS!!\033[m'.center(62))
        linha()
        print(f'A palavra era: {PALAVRA_SECRETA}')
        print(f'Tentativas: {tentativas}')
        if tentativas < 10:
            print('UAU!!!')
        elif tentativas < 12:
            print('Foi bem!')
        elif tentativas < 15:
            print('Dá pra melhorar!')
        else:
            print('Nota DÓ!')
        # reinicia os dados
        tentativas = 0
        letras_tentadas = list()
        letras_acertadas = list()
