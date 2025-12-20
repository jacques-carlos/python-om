"""

MÉTODOS ESTÁTICO / STATIC METHOD

"""
from datetime import date
from random import randint


class Pessoa:
    ano_atual = date.today().year                           # variável de classe

    def __init__(self, nome, idade):                        # construtor
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):                           # método de instância
        print(self.ano_atual - self.idade)

    @classmethod                                            # decorador
    def por_ano_nascimento(cls, nome, ano_nascimento):      # método de classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod                                           # método estático
    def gera_id():
        id = randint(10000, 99999)
        return id


# criando um objeto a partir de um construtor
p1 = Pessoa('João', 32)
print(p1.nome, p1.idade)
# embora seja independente de classe ou objeto, o método estático é chamado pela classe
print(f'ID:{Pessoa.gera_id()}')

# criando um objeto a partir de um método de classe
p2 = Pessoa.por_ano_nascimento('João', 1993)
print(p2.nome, p2.idade)
# o método estático também funciona sendo chamado por uma instância
print(f'ID:{p2.gera_id()}')
