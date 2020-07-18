matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


for i in range(3, 11):#vai da linha 3 até a linha 11, lembrando que fica 11 - 1 = 10, isso no python
    matriz[i][11 - i] = '\033[4;30;43mE\033[m'
#deslocamento de coluna para esquerda, faz soma de coluna + linha
# coluna = 8   subtração = 8 + 3 = 11
# linha = 3     resposta = matriz[i][11 - i] = 'E'

for i in range(2, 11):#vai da linha 2 até a linha 11, lembrando que fica 11 - 1 = 10, isso no python
    matriz[i][i + 7] = '\033[4;30;43mD\033[m'
#deslocamento de coluna para direita, faz subtração de coluna - linha
#coluna = 9    subtração = 9 - 2 = 7
#linha = 2     resposta = matriz[i][i + 7] = 'D'

for i in range(0, 20):
    matriz[11][i] = '\033[4;30;43mH\033[m'  # linha


k = 0
while k < 14:
    f = 0
    while f < 20:
        print(matriz[k][f], end=' ')
        f = f + 1
    print()
    k = k + 1
