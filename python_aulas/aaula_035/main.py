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
- MÉTODOS ESTÁTICOS

"""
from pessoa import Pessoa

p1 = Pessoa('Irineu', 50)  # criando objeto
p2 = Pessoa('Creuza', 55)  # criando objeto

print(p1.ano_atual)  # printando ano atual (variável de classe)
print(Pessoa.ano_atual)  # printando ano atual (variável de classe)

# utilizando os atributos do objeto
print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}.')
# utilizando os atributos do objeto
print(f'{p2.nome} nasceu em {p2.get_ano_nascimento()}.')

p1.falar('motos')  # método de instância
p2.falar('carros')  # método de instância
p1.comer('pizza')  # método de instância
