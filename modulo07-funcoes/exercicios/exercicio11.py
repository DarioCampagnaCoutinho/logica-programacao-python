def calcular(numeros):
    soma = 0
    for i in range(1, numeros + 1, 3):
        soma += i
        print(soma)


calcular(5)