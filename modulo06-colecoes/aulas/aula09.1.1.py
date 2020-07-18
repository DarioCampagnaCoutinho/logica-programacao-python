matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

i = 0
while i < 5:
    j = 4 - i
    while j  < 5:
        matriz[i][j] = '\033[4;30;43mX\033[m'
        j = j + 1
    i = i + 1


k = 0
while k < 5:
    f = 0
    while f < 5:
        print(matriz[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1
