def fatorial(numero):
    fat = 1
    for i in range(1, numero + 1):
        fat = fat * i
    return fat

r = fatorial(5)
print(r)