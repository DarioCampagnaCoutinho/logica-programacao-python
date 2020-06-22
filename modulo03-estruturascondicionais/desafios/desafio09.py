numero = str(input('Iforme um NÙMERO : '))

print('1 - Binário')
print('2 - Octal')
print('3 - Hexdecimal')

opcao = str(input('Informe uma das opções?'))

if opcao == '1':
    print(int(numero, 2))
elif opcao == '2':
    print(int(numero, 8))
elif opcao == '3':
    print(int(numero, 16))