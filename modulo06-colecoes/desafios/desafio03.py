lista_de_listas_inteiros = [
    [1, 2, 1, 4, 4, 5, 6, 6, 9, 1],
    [0, 2, 3, 4, 4, 5, 5, 6, 9, 8],
    [7, 1, 3, 3, 4, 10, 6, 0, 9, 8],
    [7, 2, 3, 3, 4, 5, 6, 6, 9, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 1, 3, 2, 4, 6, 3, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 5, 8, 9, 10],
    [1, 2, 3, 0, 0, 6, 4, 8, 9, 10],
    [10, 2, 3, 5, 5, 6, 3, 8, 9, 10],
    [0, 2, 3, 4, 4, 6, 8, 8, 9, 9]
]


def encontra_primeiro_duplicado(paran_listas_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in paran_listas_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    return primeiro_duplicado


for lista_inteiro in lista_de_listas_inteiros:
    print(lista_inteiro, encontra_primeiro_duplicado(lista_inteiro))
