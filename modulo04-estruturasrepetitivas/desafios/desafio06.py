t1 = 0
t2 = 1
t3 = 0
print(t1, t2, end= ' ')
for contador in range(10):
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3