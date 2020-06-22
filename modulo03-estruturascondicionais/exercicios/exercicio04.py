salario = float(input('Salário = '))
prestacao = float(input('Valor da prestação = '))

diferenca = salario - (salario / 100 * 20)

porcentagem = salario - diferenca

if prestacao < porcentagem:
    print('Prestação Aceita!')
else:
    print('Prestação não Aceita!')