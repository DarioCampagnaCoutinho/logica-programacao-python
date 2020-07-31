def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi{nome}'


def saudacao(nome, saudacao):
    return f'Olá {nome} {saudacao}'


executando1 = mestre(fala_oi, ' Dario')
print(executando1)

executando2 = mestre(saudacao, 'Dario', 'Campagna')
print(executando2)

executando3 = mestre(saudacao, 'Dario', saudacao='Campagna')
print(executando3)