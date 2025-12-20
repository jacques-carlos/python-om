"""

Introdução ao Try/Except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Digite um número para dobrar: ')

# Fail fast
try:
    numero_float = float(numero_str)
except:
    print('Isso não é um número!')
else:
    print(f'O dobro de {numero_float} é {numero_float * 2}')
finally:
    print('Encerrando programa...')
