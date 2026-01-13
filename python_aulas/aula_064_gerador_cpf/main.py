"""

Gerador de CPF

"""
from random import randint

cpf_nove_digitos = ''
for contador in range(9):
    digito = randint(0, 9)
    cpf_nove_digitos += str(digito)

# Caso o sistema gere um CPF de 9 dígitos repetidos:
if cpf_nove_digitos[0] * 9 == cpf_nove_digitos:
    print('ERRO! O sistema gerou um CPF base com 9 números iguais. Reinicie o programa.')
    quit()

resultado_1 = 0
multiplicador_1 = 10
for digito in cpf_nove_digitos:
    resultado_1 += int(digito) * multiplicador_1
    # A cada dígito que passa, o multiplicador diminui 1
    multiplicador_1 -= 1

# Multiplica por 10, Divide por 11 e pega o resto
resultado_1 = (resultado_1 * 10) % 11

digito_1 = '0' if resultado_1 > 9 else str(resultado_1)

# Os primeiros dez dígitos são necessários para o segundo verificador
cpf_dez_digitos = cpf_nove_digitos + digito_1

resultado_2 = 0
multiplicador_2 = 11
for digito in cpf_dez_digitos:
    resultado_2 += int(digito) * multiplicador_1
    # A cada dígito que passa, o multiplicador diminui 1
    multiplicador_2 -= 1

# Multiplica por 10, Divide por 11 e pega o resto
resultado_2 = (resultado_2 * 10) % 11

digito_2 = '0' if resultado_2 > 9 else str(resultado_2)

cpf = cpf_dez_digitos + digito_2

print(f'O CPF gerado foi: {cpf}')
