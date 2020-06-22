numero = 1234
numero = str(numero)

soma = 0

for i in range(len(numero)):
    soma += int(numero[i])

print(soma)