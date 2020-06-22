print("===== Desafio 15 =====")
dias = int(input('Dias = '))
km = float(input('Km = '))

total = (dias * 60) + (km * 0.15)

print('Total a pagar R$ {:.2f} '.format(total))
