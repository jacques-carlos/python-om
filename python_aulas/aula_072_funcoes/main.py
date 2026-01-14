"""

Exercício com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.

"""


def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(10, 5, 4)
print(f'O resultado da multiplicação é {multiplicacao}')


def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é PAR'
    return f'{numero} é ÍMPAR'


print(par_impar(105))
print(par_impar(202))
