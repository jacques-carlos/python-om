# while/else

string = 'Valor qualquer'
i = 0

while i < len(string):
    letra = (string[i])
    print(letra)
    i += 1
    # break -> o else não é executado
else:
    print('Dentro do while (o else foi executado).')

print('Fora do while.')
