minha_string = 'O rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''
nova_string = ''
while c < tamanho_string:
    if minha_string[c] == 'r':
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    #print(nova_string) string é montada um aum
    c+=1
print(nova_string)
