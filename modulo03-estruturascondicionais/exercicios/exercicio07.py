num1 = int(input('Número 1 = '))
num2 = int(input('Número 2 = '))
num3 = int(input('Número 3 = '))

if num1 >= num2 and num1 >= num3:
    print('Número {} é o maior!'.format(num1))
elif num2 >= num1 and num2 >= num3:
    print('Número {} é o maior!'.format(num2))
else:
    print('Número {} é o maior!'.format(num3))