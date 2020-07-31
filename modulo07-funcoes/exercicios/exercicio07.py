from math import sqrt


def entrada():
    n = int(input('Digite um número:'))
    return n


def raiz(n):
    return sqrt(n)


def mostra(n):
    print(n)


def menu():
    n = entrada()
    r = raiz(n)
    mostra(r)

menu()