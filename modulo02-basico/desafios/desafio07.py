nome = str(input('Digite seu nome : ')).strip()

print('Nome maíusculo = {}'.format(nome.upper()))
print('Nome minusculo = {}'.format(nome.lower()))
print('Total de {} letras'.format(len(nome) - nome.count(' ')))

dividir = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividir[0], len(dividir[0])))