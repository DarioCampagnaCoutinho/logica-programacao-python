numero = 1923

u = numero % 10
d = (numero % 100) // 10
c = (numero // 100) % 10
m = numero // 1000

print('Unidade = {}'.format(u))
print('Dezena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))