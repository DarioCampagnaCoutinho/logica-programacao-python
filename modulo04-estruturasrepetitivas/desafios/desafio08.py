for i in range(1, 101):
    div = 0
    for j in range(1, i + 1):
        resto = i % j
        if resto == 0:
            div += 1
    if div == 2:
        print('Número {} é PRIMO!'.format(i))
    else:
        print('Número {} não é PRIMO!'.format(i))
