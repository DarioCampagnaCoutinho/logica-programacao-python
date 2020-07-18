"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""


lista = []

for i in range(8):
    lista.append(i)

x = int(input('X = '))
y = int(input('Y = '))

print(f'Soma = {lista[x] + lista[y]}')