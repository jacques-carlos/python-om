"""

ASSOSSIAÇÃO

"""
from classes import Escritor
from classes import Caneta
from classes import MáquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
máquina = MáquinaDeEscrever('Antiga')

print(escritor.nome)
print(caneta.marca)
print(máquina.modelo)

caneta.escrever()
máquina.escrever()

#exemplo 1
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
#exemplo 2
escritor.ferramenta = máquina
escritor.ferramenta.escrever()

del escritor #embora o objeto 'escritor' tenha sido apagado, os objetos 'caneta' e 'máquina' continuam funcionando, mesmo que antes associados
#print(escritor.nome)
print(caneta.marca)
máquina.escrever()