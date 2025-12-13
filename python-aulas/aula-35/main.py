"""

- OBJETO(INSTÂNCIA)
- CLASSE > molde para o objeto
- instanciar > processo de criação de um objeto a partir de uma classe
- VARIÁVEL > atributo de um objeto/classe
- MÉTODO > função que pertece a um objeto/classe

- VARIÁVEIS DE INSTÂNCIA > exemplo: > p1.nome
- MÉTODOS DE INSTÂNCIA > exemplo > p1.andar
- VARIÁVEIS DE CLASSE
- MÉTODOS DE CLASSE

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