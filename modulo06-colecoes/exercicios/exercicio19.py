lista = []

for i in range(1, 50):
    lista.append((i + 5 * i) % (i + 1))

for i in lista:
    print(i)