"""

ENCAPSULAMENTO
atributos e métodos
public, protected, private
_       "protected"                  objeto._atributo
__      "private"                    objeto._Classe__atributo

"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}


    #getter > método da classe que vai retornar os dados (atributo) da instância
    @property
    def dados(self):
        return self.__dados


    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})


    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def deletar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Luiz')
bd.inserir_cliente(4, 'Rose')
bd.listar_clientes()
print('='*50)
bd.deletar_cliente(3)
bd.deletar_cliente(4)
bd.listar_clientes()
print('='*50)
bd.__dados = 'Qualquer coisa'         #quebra da classe > para de funcionar > por isso usar encapsulamento

bd.listar_clientes()
print('='*50)
print(bd.__dados)
print('='*50)
print(bd._BaseDeDados__dados)
print('='*50)
print(bd.dados) #não posso configurar esse atributo pois não há um setter