numero1 = int(input("Número 1 = "))
numero2 = int(input("Número 2 = "))

if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
    print('Diferença = {}'.format(numero1 - numero2))
else:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
    print('Diferença = {}'.format(numero2 - numero1))