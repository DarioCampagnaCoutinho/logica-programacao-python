matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

for i in range(5):
    matriz[2][i] = '\033[4;30;43mX\033[m'#linha

for i in range(2, 5):
    matriz[i][2] = '\033[4;30;43mX\033[m'#coluna

k = 0
while k < 5:
    f = 0
    while f < 5:
        print(matriz[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1
