"""

*args
Argumentos não nomeados (empacotamento e desempacotamento)

"""


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


numeros = 78, 26, 109, 222

soma_numeros = soma(*numeros)
print(f'A soma dos números é: {soma_numeros}')

# função nativa do Python para somar:
print('A soma dos números é:', sum(numeros))
