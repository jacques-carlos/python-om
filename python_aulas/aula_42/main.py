"""

AGRAGAÇÃO

"""
from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto1 = Produto('Camiseta', 50)
produto2 = Produto('Iphone', 10000)
produto3 = Produto('Caneca', 15)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.listar_produtos()
print(carrinho.soma_total())
