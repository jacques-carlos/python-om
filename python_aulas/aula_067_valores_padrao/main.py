"""

Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Ao definir um parâmetro com valor padrão, todos os próximos parâmetros deverão ter valor padrão

Refatorar: editar o seu código.

"""


def soma(x, y, z=None):
    if z is None:
        print(f'{x=} {y=}', 'x + y =', x + y)
    else:
        print(f'{x=} {y=} {z=}', 'x + y + z=', x + y + z)


soma(1, 2)
soma(3, 4, 5)
