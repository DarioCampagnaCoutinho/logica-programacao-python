horaInicial = int(input('Hora Inicial :'))
horaFinal = int(input('Hora Final :'))

duracao = 0

if horaInicial < horaFinal:
    duracao = horaFinal - horaInicial
else:
    duracao = 24 - horaInicial + horaFinal

print('O jogo Durou {} horas.'.format(duracao))