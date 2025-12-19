# Operador Lógico or
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada como verdadeira.
# truthy vs falsy
# São considerados falsy: 0 0.0 '' False etc.
# None: representa um não valor (inexistente)

entrada = input('Entrar[E] Sair[S]: ')
if entrada in 'Ee':
    senha_digitada = input('Senha: ')
senha = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha:
    print('Entrar')
else:
    print('Sair')
