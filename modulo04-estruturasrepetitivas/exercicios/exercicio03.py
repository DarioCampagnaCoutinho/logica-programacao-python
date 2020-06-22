print('-=-'*7)
print('-=-  Calculadora  -=-')
print('-=-'*7)

from time import sleep

while True:
    num1 = input('Digite o 1° número = ')
    num2 = input('Digite o 2° número = ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite Novamente')
        continue

    num1 = int(num1)
    num2 = int(num2)

    operacao = input('Operação = ')

    if operacao == '+':
        print('Soma = {}'.format(num1 + num2))
    elif operacao == '-':
        print('Subtração = {}'.format(num1 - num2))
    elif operacao == '-':
        print('Multiplicação = {}'.format(num1 * num2))
    elif operacao == '/':
        print('Divisão = {}'.format(num1 / num2))

    opcao = input('Sair (S) == Continuar (C)').upper()
    if opcao == 'S':
        print('Encerrrando o programa....')
        sleep(5)
        break
    elif opcao == 'C':
        continue