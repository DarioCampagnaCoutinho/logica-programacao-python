minha_string = 'O rato roeu a roupa do rei de roma'
c = 0
tamanho_string = len(minha_string)
nova_string = ''
while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    print(nova_string)

    c+=1

print(nova_string)
