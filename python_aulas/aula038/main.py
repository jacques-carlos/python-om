"""

GUETTERS E SETTERS

"""
class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


    def desconto(self, percentual):
        self.preço = self.preço - ((self.preço*percentual)/100)


    # Getter
    @property
    def preço(self):
        return self._preço
    
    
    # Setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))      
        self._preço = valor


    # Getter
    @property
    def nome(self):
        return self._nome
    

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preço)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preço)