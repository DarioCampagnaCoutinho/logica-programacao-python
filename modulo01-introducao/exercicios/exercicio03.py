from math import pow, sqrt

a = float(input('Valor de A : '))
b = float(input('Valor de B : '))

hipotenusa = sqrt(pow(a, 2) + pow(b, 2))

print('Hipotenusa = {:.3f}'.format(hipotenusa))
