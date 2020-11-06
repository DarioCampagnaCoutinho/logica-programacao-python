class Televisao:
    def __init__(self, ligada, canal, min, max):
        self.marca = 'Samsung'
        self.tamanho = 500
        self.ligada = ligada
        self.canal = canal
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if (self.canal -1 >= self.cmin):
            self.canal -= 1

    def muda_canal_para_cima(self):
        if (self.canal + 1 <= self.cmax):
            self.canal += 1


tv = Televisao(True, 3, 1, 99)

for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)