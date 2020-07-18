cpf = '16899535009'
novo_cpf = cpf[:-2]

total1 = 0
reverso1 = 10
digito1 = 0
for index in range(len(novo_cpf)):
    total1 += int(novo_cpf[index]) * reverso1
    reverso1 -= 1
digito1 = 11 - (total1 % 11)
if digito1 > 9:
    digito1 = 0
    print(digito1)

total2 = 0
reverso2 = 11
digito2 = 0
for index in range(len(novo_cpf)):
    total2 += int(novo_cpf[index]) * reverso2
    reverso2 -= 1
digito2 = 11 - (total2 % 11)
print(digito2)

novo_cpf += str(digito1) + str(digito2)
print(novo_cpf)

if novo_cpf == cpf:
    print("O CPF é verdadeiro!")
else:
    print("O CPF não é verdadeiro!")

