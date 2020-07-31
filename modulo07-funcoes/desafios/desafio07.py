def soma(lista):
    total = 0
    for e in lista:
        total += e
    return total


def media(lista):
    return (soma(lista) / len(lista))


lista = list(range(1, 10))
print(media(lista))