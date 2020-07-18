a = []
b = []
c = []

for i in range(3):
    a.append(int(input('Números de A :')))

for j in range(3):
    b.append(int(input('Números de B :')))

for y in range(3):
    c.append(a[y] - b[y])

print(c)