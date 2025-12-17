class A:
    vari =  123

    def __init__(self):
        self.vari = 321


a1 = A()
a2 = A()

#o interpretador busca a variável primeiro na instância, depois na classe.
print(a1.vari)
print(a2.vari)
print(A.vari)



class B:
    vari = 123

    def __init__(self):
        pass


b1 = B()
b2 = B()

#essa é melhor maneira de alterar uma variável em todos os objetos: utilizando uma variável de classe
B.vari = 'Alterado'

print(b1.vari)
print(b2.vari)
print(B.vari)