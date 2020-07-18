matriz = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

for i in range(3):
    for j in range(1, 5):
        matriz[i][j] = 'X'

k = 0
while k < 5:
    f = 0
    while f < 5:
        print(matriz[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1
