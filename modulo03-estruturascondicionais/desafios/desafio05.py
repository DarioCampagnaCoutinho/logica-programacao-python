distancia = float(input('Qual a distância da sua viagem?'))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Voçê está prestes a começar uma viagem de {} km.'.format(distancia))
print('O preço da sua viagem é R$ {:.2f} '.format(preco))