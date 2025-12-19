"""

Formatação básica de strings:
f-strings:
x ou X -> hexadecimais
Conversion flags -> !r !s !a

"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:-^10}.')  # preenchendo com caracteres
print(f'{145750.438191032:,.2f}.')  # organizando por milhar
print(f'O hexadecimal de 9999 é {9999:08X}')
