print("===== Desafio 13 =====")
salario = float(input('Digite o sálario = '))
porcentagem = int(input('Digite o aumento ='))

novo = salario + (salario * porcentagem / 100)

print('O sálario atual é de {} R$, com o aumento de {} %, o novo sálario é de {:.2f} R$'.format(salario, porcentagem, novo))


