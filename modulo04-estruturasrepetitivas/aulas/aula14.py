minha_string = 'O rato roeu a roupa do rei de roma'
tamanho_string = len(minha_string)

c = 0
contagem = 0
letra = ''
while c < tamanho_string:
    conta = minha_string.count(minha_string[c])
    print(conta, minha_string[c])
    c+=1
