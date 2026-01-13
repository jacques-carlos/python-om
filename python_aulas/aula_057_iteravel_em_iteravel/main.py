"""

Iterável dentro de interável (e seus índices)

"""

grupos = [

    ['Maria', 'Helena', 'Borges'],  # 0

    ['Elaine', 'Douglas', 'Cristiane'],  # 1

    ['Luiza', 'João', 'Eduarda']  # 2

]

# print(grupos[0])  # Acessando o grupo 0
# print(grupos[2][1])  # Acessando o João
# print(grupos)  # Acessando todos os grupos

for numero, grupo in enumerate(grupos):
    print('Grupo', numero)
    for aluno in grupo:
        print('Aluno:', aluno)
