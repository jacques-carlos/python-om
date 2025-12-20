class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereços = []

    def inserir_endereço(self, cidade, estado):
        self.endereços.append(Endereço(cidade, estado))

    def listar_endereços(self):
        for endereço in self.endereços:
            print(endereço.cidade, endereço.estado)


class Endereço:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
