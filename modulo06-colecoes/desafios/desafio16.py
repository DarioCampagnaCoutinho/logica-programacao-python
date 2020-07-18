matriz = [[0 for i in range(2)] for j in range(2)]

for linha in range(2):
    for coluna in range(2):
        matriz[linha][coluna] = int(input('Números : '))
for linha in range(2):
    for coluna in range(2):
        print("%4d" % matriz[linha][coluna], end='')
    print()