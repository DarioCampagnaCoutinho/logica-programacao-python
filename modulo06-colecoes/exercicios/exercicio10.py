"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

lista = []

for i in range(10):
    lista.append(int(input('Digite um número : ')))

cont = 0
for i in lista:
    if i % 2 == 0:
        cont += 1

print(f'Total de Pares : {cont}')