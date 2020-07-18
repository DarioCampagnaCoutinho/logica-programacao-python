"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""

lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

print(f"\nO maior elemnto do vetor é: {max(lista)}")
print(f"O menor elemento do vetor é: {min(lista)}")

maior = 0
menor = min(lista)

for i in lista:
    if i > maior:
        maior = i

    print(i, end=' ')
print()
print('Maior : ', maior)
print('Menor : ', menor)