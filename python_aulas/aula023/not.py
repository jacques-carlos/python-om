# Operador lógico not
# Usado para inverter expressões
# not True = False
# not False = True

print(not True)  # False
print(not False)  # True

# ex.:
senha = (input('Senha: '))

if not senha:
    print('Você não digitou nada.')
else:
    print(f'Sua senha é: {senha}.')
