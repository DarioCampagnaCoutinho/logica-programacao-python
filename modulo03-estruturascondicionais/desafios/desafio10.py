peso = float(input('Digite o PESO:'))
altura = float(input('Digite a ALTURA : '))

resultado = peso / (altura ** 2)

if resultado < 18.6:
    print('Abaixo do Peso!')
elif resultado >= 18.6 and resultado < 25:
    print('Saudável!')
elif resultado >= 25 and resultado < 30:
    print('Peso em Excesso!')
elif resultado >= 30 and resultado < 35:
    print('Obesidade Grau 1!')
elif resultado >= 35 and resultado < 40:
    print('Obesidade Grau 2!')
else:
    print('Obesidade Móbida!')