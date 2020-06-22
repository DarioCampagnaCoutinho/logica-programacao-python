num = int(input('Digite um número:'))

div = 0
for i in range(1, num + 1):
    resto = num % i
    print(resto)
    if resto == 0:
        div += 1
if div == 2:
    print('Número {} é PRIMO!'.format(num))
else:
    print('Número {} não é PRIMO!'.format(num))
