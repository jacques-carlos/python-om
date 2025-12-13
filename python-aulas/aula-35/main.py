"""

- objeto
- classe > molde para o objeto
- instanciar > processo de criação de um objeto a partir de uma classe
- variável da instância > atributo do objeto > exemplo: > p1.nome
- variável da classe
- metódo >  comportamento do objeto > exemplo > p1.andar
- os métodos são funções que pertecem a um objeto/classe

"""
from pessoa import Pessoa

p1 = Pessoa('Irineu', 50)
p2 = Pessoa('Creuza', 55)

print(p1.ano_atual)
print(Pessoa.ano_atual)

print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}.')
print(f'{p2.nome} nasceu em {p2.get_ano_nascimento()}.')

p1.falar('motos')
p2.falar('carros')
p1.comer('pizza')