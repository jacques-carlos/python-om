"""

Operador Lógico and
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
truthy vs falsy
São considerados falsy: 0 0.0 '' False etc.
None: representa um não valor (inexistente)

"""

entrada = input('Entrar[E] Sair[S]: ')
if entrada == 'E':
    senha_digitada = input('Senha: ')
senha = '123456'

if entrada == 'E' and senha_digitada == senha:
    print('Entrar')
else:
    print('Sair')
