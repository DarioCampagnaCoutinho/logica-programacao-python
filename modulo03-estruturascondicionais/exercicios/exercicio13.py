numero = input('Número : ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é PAR.')
    else:
        print(f'{numero} é IMPAR.')
else:
    print('Digite um número')