i = 0
j = 1
for contador in range(7):
    print(i, end= ' ')  # 0 1 1
    i = i + j # 0 + 1 = 1  i = 1   1 + 0 = 1   i = 1  1 + 1 = 2
    j = i - j # 1 - 1 = 0  j = 0   1 - 0 = 1   j = 1  2 - 1 = 1