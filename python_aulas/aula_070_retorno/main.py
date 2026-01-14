"""

Retorno de valores das funções (return)

"""


def soma(x, y):
    if x > 10:
        return 'X muito grande!'
    return x + y


soma1 = soma(2, 2)
soma2 = soma(3, 3)
soma3 = soma(soma1, soma2)
print(soma3)

soma4 = soma(15, 5)
print(soma4)
