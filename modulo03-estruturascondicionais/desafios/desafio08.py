valor_casa = float(input('Valor da casa : '))
salario = float(input('Salário : '))
anos = int(input('Total de anos : '))

total_prestacoes = (anos * 12)
valor_pretacao = valor_casa / total_prestacoes
valor_porcentagem = salario / 100 * 30

if valor_pretacao < valor_porcentagem:
    print('Empréstimo Concedido')
else:
    print('Empréstimo Negado')

print('30 % do SALÀRIO = R$ {:.3f}'.format(valor_porcentagem))
print('Total de Prestações = {:.3f}'.format(total_prestacoes))
print('Valor de uma Pretação = R$ {:.3f}'.format(valor_pretacao))
print('Valor da casa = R$ {:.3f}'.format(valor_casa))