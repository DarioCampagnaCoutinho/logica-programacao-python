salario = float(input('Digite um salário? R$'))

if salario <= 1250:
    aumento = (salario * 15) / 100
    total_aumento = salario + aumento
    print('Salário = {}'.format(total_aumento))
else:
    aumento = (salario * 10) * 100
    total_aumento = salario + aumento
    print('Salário = {}'.format(total_aumento))