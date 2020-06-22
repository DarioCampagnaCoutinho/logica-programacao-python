nome = str(input('Nome :')).upper().strip()

print('A letra A aparece {} vezes. '.format(nome.count('A')))
print('A primeira letra A aparece na primeira posição {}'.format(nome.index('A')))
print('A ultima letra A aparece na última posição {}'.format(nome.rindex('A')))

print('A primeira letra A aparece na primeira posição {}'.format(nome.find('A')))
print('A ultima letra A aparece na última posição {}'.format(nome.rfind('A')))