class A:
    vari = 123


a1 = A()
a2 = A()

print(a1.vari)  # imprimindo a partir de uma instância
print(a2.vari)
print(A.vari)  # imprimindo diretamente da classe

A.vari = 321  # altera a variável da classe já existente (altera para todos)

print(a1.vari)
print(a2.vari)
print(A.vari)

# cria a variável para a instância (altera apenas para aquela instância)
a1.vari = 555

print(a1.vari)
print(a2.vari)
print(A.vari)

# o interpretador busca a variável primeiro na instância, depois na classe.
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
