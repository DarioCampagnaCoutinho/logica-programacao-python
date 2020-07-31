def aumento(numero, valor):
    resultado = numero * valor / 100
    return resultado + numero

resultado = aumento(100, 50)
print(resultado)