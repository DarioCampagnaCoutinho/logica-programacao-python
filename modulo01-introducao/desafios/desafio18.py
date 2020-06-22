nome = 'Dario'
idade = 35
altura = 1.76
e_maior = idade > 18
peso = 86.7
imc = peso / (altura ** 2)
ano_nascimento = 2020 - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} é {imc :.2f}')
print(f'{nome} nasceu em {ano_nascimento}')

v = '5.5'
vs = (int(float(v)))
print(type(vs))
