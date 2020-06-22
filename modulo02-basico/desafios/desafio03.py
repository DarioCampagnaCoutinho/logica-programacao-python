from math import sin, cos, tan, radians

angulo = float(input('Informe em Graus = '))

print('Seno = {:.2f}'.format(sin(radians(angulo))))
print('Cosseno = {:.2f}'.format(cos(radians(angulo))))
print('Tangente = {:.2f}'.format(tan(radians(angulo))))