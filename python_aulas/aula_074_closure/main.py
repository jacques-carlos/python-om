"""

Closure e funções que retornam outras funções

"""


def criar_saudacao(mensagem):
    def saudar(nome):
        return f'{mensagem}, {nome}!'
    return saudar


bom_dia = criar_saudacao('Bom dia')
boa_noite = criar_saudacao('Boa noite')

print(bom_dia('Jack'))
print(boa_noite('Jack'))

for nome in ('Maria', 'Joana', 'Luiz'):
    print(bom_dia(nome))
    print(boa_noite(nome))
