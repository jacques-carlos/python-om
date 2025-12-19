class Pessoa:  # superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.nome = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):  # subclasse
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')
