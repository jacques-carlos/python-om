"""

Exercício

Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

"""


def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
