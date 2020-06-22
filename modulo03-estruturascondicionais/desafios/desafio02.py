velocidade = input('Digite a velocidade : ')

if velocidade.isdecimal():
    velocidade = float(velocidade)
    if velocidade > 80:
        multa = (velocidade - 80) * 7
        print("Voçê foi multado, pois velocidade é de {} Km/h".format(velocidade))
        print("E o valor da multa é {} R$".format(multa))
    else:
        print("Tudo Normal")
else:
    print("Atenção!")
    print("Digie um número válido")