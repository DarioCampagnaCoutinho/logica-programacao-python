horas = int(input('Horas:'))

if horas >= 0 and horas <= 11:
    print('Bom Dia')
elif horas >= 12 and horas <= 17:
    print("Boa Tarde")
elif horas >= 18 and horas <= 23:
    print("Boa Noite")
else:
    print("Digite Novamente")
