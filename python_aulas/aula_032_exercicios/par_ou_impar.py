"""

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

str_numero = input('Digite um número inteiro: ')

try:
    int_numero = int(str_numero)
    numero_e_par = int_numero % 2 == 0

except:
    print('Esse valor não é um número inteiro.')

else:
    if numero_e_par:
        print('Esse número é par.')
    else:
        print('Esse número é ímpar.')
