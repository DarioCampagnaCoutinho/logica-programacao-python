lista = []
verifica = []

for i in range(10):
    lista.append(int(input("Digite um valor: ")))

    if lista[i] in verifica:
        print(f"Já existe o valor {lista[i]} no vetor")

    verifica.append(lista[i])

print(verifica)
