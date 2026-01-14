"""

Higher Order Functions
Funções que podem receber e/ou retornar outras funções

Com funções nós podemos:
    Jogá-las em variáveis
    Passá-las como parâmetros para outras funções
    Retorná-las dentro de outras funções

"""


def saudacao(mensagem, nome):
    return f'{mensagem}, {nome}!'


def executar(funcao, *args):
    return funcao(*args)


print(executar(saudacao, 'Olá', 'Mundo'))
print(executar(saudacao, 'Tchau', 'Galera'))
