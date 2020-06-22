distancia = float(input('Qual a distância da sua viagem?'))

if distancia <= 200:
    resultado = distancia * 0.50
    print('Voçê está prestes a começar uma viagem de {} km.'.format(distancia))
    print('O preço da sua viagem é R$ {:.2f} '.format(resultado))
else:
    resultado = distancia * 0.45
    print('Voçê está prestes a começar uma viagem de {} km.'.format(distancia))
    print('O preço da sua viagem é R$ {:.2f} '.format(resultado))