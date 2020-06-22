from math import sqrt, pow

x = float(input('Número 1 = '))
y = float(input('Número 2 = '))
z = float(input('Número 3 = '))

opcao = str(input('Opção : '))

if opcao == 'pd':
    ponderada = (x + (3 * y) + (3 * z)) / 6
    print('Resultado Ponderada = {:.2f}'.format(ponderada))
elif opcao == 'hr':
    harmonica = 1 / ((1 / x) + (1 / y) + (1 / z))
    print('Resultado Harmônica = {:.2f}'.format(harmonica))
elif opcao == 'gm':
    geometrica = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
    print('Resultado Geométrica = {:.2f}'.format(geometrica))
else:
    print('Execute novamente o programa, opção inválida')
