def numeros(x, y):
    return x % y == 0 or y % x == 0


def multiplos(x, y):
    if numeros(x, y):
        return True
    else:
        return False

print(numeros(10, 5))
print(numeros(10, 3))

