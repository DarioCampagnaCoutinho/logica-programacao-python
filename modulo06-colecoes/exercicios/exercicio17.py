lista = []

soma = 0
media = 0

for i in range(1, 6):
    lista.append(float(input('Nota :')))

for i in lista:
    soma += i

media = soma / len(lista)

print('Soma = {}'.format(soma))
print('Media = {}'.format(media))