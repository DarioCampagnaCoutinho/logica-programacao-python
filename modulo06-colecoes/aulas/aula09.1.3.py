matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

i = 0
while i < 5:
    j = 7 - i
    while j < i + 4:
        matriz[i][j] = '\033[4;30;43mX\033[m'
        j = j + 1
    i = i + 1

for m in range(5, 8):
    matriz[m][5] = '\033[4;30;43mX\033[m'

k = 0
while k < 8:
    f = 0
    while f < 11:
        print(matriz[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1