lista = []
pares = []
impares = []

for i in range(1, 16):
    lista.append(i)

for i in lista:
    j = i / 2
    print(j, end=', ')
    if j % 2 == 0:
        pares.append(j)
    else:
        impares.append(j)

for s in pares:
    print('\n', s)