from datetime import date

class Pessoa:
    ano_atual = date.today().year                                           #variável da classe

    def __init__(self, nome, idade, comendo=False, falando=False):          #construtor 
        self.nome = nome                                                    #variável/atributo de um objeto
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    

    def comer(self, alimento):                                              #método de instância
        if self.falando:
            print(f'{self.nome} não pode comer enquanto fala.')
            return        
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return    
        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come.')
            return        
        if self.falando:
            print(f'{self.nome} já está falando.')
            return        
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return        
        print(f'{self.nome} parou de falar.')
        self.falando = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade      #não poderia ser somente "ano_atual", pois é um método de instância