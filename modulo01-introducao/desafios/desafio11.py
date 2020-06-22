print("===== Desafio 11 =====")
ladoParede = float(input('Lado parede = '))
alturaParede = float(input('Altura parede = '))

area = ladoParede * alturaParede
tintaUsada = area / 2
print('Sua parede tem a dimensão de {}X{} e sua área é de {} m'.format(ladoParede, alturaParede, area))
print('Para pintar essa parede, voçê precisará de {} litros de tintas'.format(tintaUsada))