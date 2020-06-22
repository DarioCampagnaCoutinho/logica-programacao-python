from math import sqrt

numero = int(input('Número = '))

if numero >= 0:
    print('Raiz = {}'.format(sqrt(numero)))
else:
    print('Número Inválido!')