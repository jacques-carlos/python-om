"""

Imprecisão de ponto flutuante
Double-precision floating-point- format IEEE 754
3 maneiras de corrigir:

"""

import decimal

# Maneira com imprecisão
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print('Maneira 0:', numero_3)

# MANEIRA 1: Utilizando f-strings
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print('Maneira 1:', f'{numero_3:0.1f}')

# MANEIRA 2: Utilizando a função round
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print('Maneira 2:', round(numero_3, 1))

# MANEIRA 3: Utilizando a classe Decimal do módulo decimal
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print('Maneira 3:', numero_3)
