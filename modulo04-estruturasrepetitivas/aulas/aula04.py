from math import sqrt, pow, ceil

print("Fibonacci")

i = 0
j = 1

for contador in range(0, 10):
    print(ceil(sqrt(pow(i, 3.5))), end=" ")
    i = i + j
    j = i - j


