from fractions import Fraction


def fracao(a, b):
    return Fraction(a, b)


a = fracao(1, 4)
b = fracao(2, 3)
c = fracao(2, 4)
soma = a + b + c
print(soma)