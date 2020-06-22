nome = str(input('Nome Completo : ')).strip()

dividir = nome.split()

print('Primeiro nome: {}'.format(dividir[0]))
print('Último nome: {}'.format(dividir[-1]))