lista = []

for i in range(4):
    while True:
        numero = int(input('Números : '))
        if numero in lista:
            print('Digite Novamente')
        else:
            lista.append(numero)
            break


print(lista)