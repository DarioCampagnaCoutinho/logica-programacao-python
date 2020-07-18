lista1 = []
for i in range(2):
    lista2 = []
    for j in range(2):
        num = int(input('Digite um número:'))
        lista2.append(num)
    lista1.append(lista2)

for i in range(2):
    for j in range(2):
        print(lista1[i][j], end=' ')
    print()