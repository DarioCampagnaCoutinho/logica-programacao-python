"""

POO - Atributos, atribuindo valores.

"""


class Televisao:
    def __init__(self):
        self.marca = 'Samsung'
        self.tamanho = 500
        self.ligada = False
        self.canal = 2


tv = Televisao()
print(tv.marca)
print(tv.tamanho)
print(tv.canal)
print(tv.ligada)

tv_sala = Televisao()
tv_sala.marca = 'Sony'
tv_sala.tamanho = 600
tv_sala.ligada = True
tv_sala.canal = 6
print(tv_sala.marca)
print(tv_sala.tamanho)
print(tv_sala.ligada)
print(tv_sala.canal)