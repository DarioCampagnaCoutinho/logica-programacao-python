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


for i in range(9, 2):#vai da coluna 8 até a coluna 1, lembrando que fica 11 - 1 = 10, isso no python
    matriz[11 + i][i] = '\033[4;30;43mE\033[m'
#deslocamento de coluna para esquerda, faz soma de coluna + linha
# coluna = 8   subtração = 8 + 3 = 11
# linha = 3     resposta = matriz[i][11 - i] = 'E'
'''
for i in range(9, 18):#vai da coluna 9 até a coluna 18, lembrando que fica 18 - 1 = 17, isso no python
    matriz[i - 7][i] = '\033[4;30;43mD\033[m'
#deslocamento de coluna para direita, faz subtração de coluna - linha
#coluna = 9    subtração = 9 - 2 = 7
#linha = 2     resposta = matriz[i - 7][i] = 'D'
'''
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
