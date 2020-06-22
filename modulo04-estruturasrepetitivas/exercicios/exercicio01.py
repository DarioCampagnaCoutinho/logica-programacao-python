num = int(input("Número:"))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print("{}".format(c), end=' ')
print('\nO número {} é divisel {} vezes'.format(num, tot))
if tot == 2:
    print("Número {} é PRIMO".format(num))
else:
    print("Número {} não é PRIMO".format(num))