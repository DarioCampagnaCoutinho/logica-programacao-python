from random import randint
from time import sleep

print('-=-'*18)
print('Vou pensar em um número de 0 a 5! Tente adivinhar.....')
print('-=-'*18)

numero = int(input('Em que número eu pensei?'))

computador = randint(1, 5)

print('Processando...')
sleep(5)

if numero == computador:
    print('O usuário venceu')
else:
    print('O computador venceu')

