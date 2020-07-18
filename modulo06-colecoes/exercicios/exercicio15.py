lista = []

for i in range(4):
    while True:
        numero = int(input('Números :'))
        if numero % 2 == 0:
            lista.append(numero)
            break
        else:
            print('Digite novamente, número precisa ser par!')

print(lista[::-1])