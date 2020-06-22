numero = int(input('Número : '))

if numero >= 0:
    if numero % 2 == 0:
       print('Número é par')
    else:
       print("Número é impar!")
else:
    print("Número é menor que 0")