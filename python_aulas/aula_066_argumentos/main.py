"""

Argumento nomeado: tem nome com sinal de igual
Argumento posicional (não nomeado): recebe apenas o argumento (valor)

"""


# Definição da função
def soma(x, y, z):
    print(f'{x=}, {y=}, {z=}', '|', 'x + y + z =', x+y+z)


# Nome da função
soma

# Execução da função
soma(1, 2, 3)
soma(1, y=2, z=3)  # Após um agumento nomeado, todos devem ser nomeados
