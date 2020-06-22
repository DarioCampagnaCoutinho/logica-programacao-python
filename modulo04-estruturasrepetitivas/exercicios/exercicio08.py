
num = int(input("Digite um número positivo e impar: "))

print()
if num % 2 == 1:
    print(f"Todos os números impares de 1 até {num} em ordem crescente:")
    for i in range(num+1, 0, -1):
        if i % 2 == 1:
            print(i)

else:
    print("Digite um número impar e positivo!")
