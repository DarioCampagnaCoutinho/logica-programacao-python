
num = int(input('Número = '))

for i in range(1, num):
    for j in range(1, i):
        print(j, end='')
    print()