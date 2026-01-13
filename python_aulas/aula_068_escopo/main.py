"""

Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.

"""

x = 100


def escopo():

    def outra_escopo():  # É um escopo local dentro de outro escopo local
        x = 20
        print('x =', x)

    x = 10
    print('x =', x)
    outra_escopo()


print('x =', x)
escopo()
print('x =', x)  # O valor de x não muda


############################################################################################


y = 100


def escopo():

    def outra_escopo():  # É um escopo local dentro de outro escopo local
        global y
        y = 20
        print('y =', y)

    global y
    y = 10
    print('y =', y)
    outra_escopo()


print('y =', y)
escopo()
print('y =', y)  # O valor de y muda
