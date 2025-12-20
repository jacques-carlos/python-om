# Contando de 1 até 100 de 1 em 1 e pulando os múltiplos de 7.

contador = 0

while contador < 100:
    contador += 1

    if contador % 7 == 0:
        continue

    print(contador)
