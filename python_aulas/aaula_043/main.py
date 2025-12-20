"""

COMPOSIÇÃO

"""

from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereço('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listar_endereços()
print()

cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereço('Salvador', 'BA')
cliente2.inserir_endereço('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.listar_endereços()
print()

cliente3 = Cliente('João', 19)
cliente3.inserir_endereço('São Paulo', 'SP')
print(cliente3.nome)
cliente3.listar_endereços()
print()
