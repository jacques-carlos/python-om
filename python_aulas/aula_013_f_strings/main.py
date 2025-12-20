# Formatação de Strings com f-strings

nome = 'Carlos'
altura = 1.8
peso = 65.9
imc = 65 / 1.8 ** 2  # imc = massa(kg) / (altura x altura)(m)

linha1 = f'{nome} tem {altura:.2f}m de altura,'
linha2 = f'pesa {peso:.1f} quilos e seu IMC é'
linha3 = f'{imc:.1f}'

print(linha1)
print(linha2)
print(linha3)
