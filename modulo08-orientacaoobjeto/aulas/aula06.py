"""

Herança

"""


class Animal:
    def __init__(self):
        self.acordado = False

    def acordar(self):
        self.acordado = True

    def dormir(self):
        self.acordado = False

    def esta_acordado(self):
        if self.acordado:
            estado_animal = 'Acordado'
        else:
            estado_animal = 'Dormindo'

        return 'Estado Animal : %s' %estado_animal


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)

    def iniciar_latido(self):
        self.latido = True

    def parar_latido(self):
        self.latido = False

    def obter_latido(self):
        if self.latido:
            estado_latido = 'Latindo'
        else:
            estado_latido = 'Calado'
        return 'Estado do Latido: %s'%estado_latido


class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.miado = False

    def iniciar_miado(self):
        self.miado = True

    def parar_miado(self):
        self.miado = False

    def obter_miado(self):
        if self.miado:
            estado_miado = 'Miando'
        else:
            estado_miado = 'Calado'
        return 'Estado do miado: %s'%estado_miado


cachorro = Cachorro()
cachorro.acordar()
print(cachorro.esta_acordado())
cachorro.iniciar_latido()
print(cachorro.obter_latido())

gato = Gato()
gato.acordar()
print(gato.esta_acordado())
gato.iniciar_miado()
print(gato.obter_miado())