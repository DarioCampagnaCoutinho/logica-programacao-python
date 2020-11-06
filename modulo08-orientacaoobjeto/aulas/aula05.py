class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print('Olá %s seja bem vindo!! ' %(self.nome))

    def falar_idade(self):
        print('%s sua idade %d anos.' %(self.nome, self.idade))


p1 = Pessoa('Darui', 34)
p1.saudar()
p1.falar_idade()

