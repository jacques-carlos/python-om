# Desempacotamento em chamadas de metódos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 4, 5, 'Jonas', 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, y, z = lista
print(a, b, y, z)

#
print('Maria', 'Helena', 1, 2, 3, 4, 5, 'Jonas', 'Eduarda')

# For
for item in lista:
    print(item, end=' ')
print()

#
print(*lista)
print(*tupla)
print(*string)

#
print(*string, sep='\n')
