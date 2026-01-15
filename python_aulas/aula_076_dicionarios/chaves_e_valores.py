# Manipulando chaves e valores em dicionários

pessoa = {}  # Criando um dicionário vazio

pessoa['nome'] = 'Jacques'  # Criando uma chave
pessoa['sobrenome'] = 'Santos'

chave = 'idade'  # Chave dinâmica

pessoa[chave] = 20  # Criando uma chave dinâmica

pessoa[chave] = 21  # Alterando o valor de uma chave

del pessoa['sobrenome']  # Deletando uma chave

# Método get: verifica se uma chave existe
if pessoa.get('sobrenome', None) is None:  # Por padrão retorna None
    print('Chave não existe!')
else:
    print('Chave existe!')

print(pessoa)
