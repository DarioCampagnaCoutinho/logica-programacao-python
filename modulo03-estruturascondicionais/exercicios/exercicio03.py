from math import sqrt

numero = float(input('Número = '))

if numero >= 0:
    print('Raiz = {}'.format(sqrt(numero)))
else:
    print('Dobro = {}'.format(numero * 2))
