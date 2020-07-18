lista1 = []

for i in range(3):
    lista2 = []
    for j in range(3):
        lista2.append(int(input('Numero')))
    lista1.append(lista2)

k = 0
while k < 3:
    f = 0
    while f < 3:
        print(lista1[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1

