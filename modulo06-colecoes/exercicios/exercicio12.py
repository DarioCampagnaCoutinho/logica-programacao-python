lista = []

for i in range(5):
    lista.append(int(input('Número : ')))

soma = 0
maior = 0
menor = min(lista)

for i in lista:

    if i > maior:
        maior = i

    if i < menor:
        menor = i

    soma += i

print('Maior : ', maior)
print('Indíce do maior', lista.index(maior))

print('Menor : ', menor)
print('Indíce do menor', lista.index(menor))

print('Soma = {}'.format(soma))
