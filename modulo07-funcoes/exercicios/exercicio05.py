def fb(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return f'Fizz Buzz, {numero} é divisível por 3 e 5'
    if numero % 5 == 0:
        return f'Buzz, {numero} é divisível por 5'
    if numero % 3 == 0:
        return f'Fizz, {numero} é divisível por 3'
    return numero

from random import randint

for i in range(10):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))