"""

POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema.

"""


class Televisao:
    def __init__(self):
        self.marca = 'Samsung'
        self.tamanho = 500
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


tv = Televisao()
print(tv.marca)
print(tv.tamanho)
print(tv.canal)
print(tv.ligada)
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)

tv_sala = Televisao()
tv_sala.marca = 'Sony'
tv_sala.tamanho = 600
tv_sala.ligada = True
tv_sala.canal = 6
print(tv_sala.marca)
print(tv_sala.tamanho)
print(tv_sala.ligada)
print(tv_sala.canal)