from math import sqrt, pow

a = float(input('Cateto Adjacente = '))
b = float(input('Cateto Oposto = '))

c = pow(a, 2) + pow(b, 2)

print('Hipotenusa = {:.2f}'.format(sqrt(c)))
