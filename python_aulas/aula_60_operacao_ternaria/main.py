"""

Operação ternária (condicional em uma linha)
<valor> if <condição> else <outro valor>

"""

dia = True
print('Bom dia!' if dia else 'Boa noite!')
# ou
print('Bom dia!') if dia else print('Boa noite!')

condicao = 10 == 11
resposta = 'Verdadeira' if condicao else 'Falsa'
print('A resposta é:', resposta)
