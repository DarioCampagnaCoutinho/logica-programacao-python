from math import sqrt, pow

a = []
b = []
c = []
d = []

for i in range(3):
    a.append(int(input('Números de A :')))

for j in range(3):
    b.append(int(input('Números de B :')))

for y in range(3):
    c.append(a[y] + b[y])

for k in c:
    d.append(pow(k, 3))

print(d)

for k in d:
    print(sqrt(k))