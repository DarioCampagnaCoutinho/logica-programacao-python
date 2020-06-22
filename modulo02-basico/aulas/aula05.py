num1 = 5
num2 = 3
num3 = 342

div = num1 / num2
print('{:.2f}'.format(div))
print(f'{div:.2f}')
print(f'{num1:0>10}')
print(f'{num1:0<10}')
print(f'{num3:0<10}')
print(f'{num3:0^10}')
print(f'{num3:0<10.2f}')

nome = 'Dario Campagna'
print((50 - len(nome)) / 2)
print(f'{nome:#^50}')
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)