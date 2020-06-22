num1 = int(input('Número 1 = '))
num2 = int(input('Número 2 = '))
num3 = int(input('Número 3 = '))

if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print("Print 1 : ",num1, num2, num3)
elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print("Print 2 : ", num2, num1, num3)
elif num3 >= num1 and num3 >= num2 and num2 >= num1:
    print("Print 3 : ",num3, num2, num1)