"""

HERANÇA SIMPLES

Associação - usa | Agregação - tem | Composição - é dono | Herança - é  

"""
from classes import *

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()
