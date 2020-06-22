minha_string = 'O rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''
while c < tamanho_string:
    conta = minha_string.count(minha_string[c])

    if contagem < conta:
        letra = minha_string[c]
        contagem = conta

    print(minha_string[c], conta)
    c+=1
