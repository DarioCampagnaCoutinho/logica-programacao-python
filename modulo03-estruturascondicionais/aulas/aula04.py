num1 = input("Número 1 = ")
num2 = input("Número 2 =")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print("Soma = {}".format(num1 + num2))
else:
    print("Não é possível somar!")