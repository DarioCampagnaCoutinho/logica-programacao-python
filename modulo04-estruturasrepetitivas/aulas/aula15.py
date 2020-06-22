minha_string = 'O rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''
while c < tamanho_string:
    qtd_vezes_letras = minha_string.count(minha_string[c])
    if contagem < qtd_vezes_letras and minha_string[c].strip():
        letra = minha_string[c]
        contagem = qtd_vezes_letras
    #print(conta, minha_string[c])
    c+=1
print(letra, contagem)
