"""

Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim

"""

condicao = True

while condicao:
    nome = input('Qual é o seu nome? ')
    if nome == 'sair':
        break
    print(f'Olá, {nome}')

print('Acabou.')
