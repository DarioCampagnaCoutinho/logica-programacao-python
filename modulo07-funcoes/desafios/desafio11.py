def calculo(nota1, nota2, nota3, letra='A'):
    if str(letra).upper() == 'A':
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return 'A média é : %.1f' % media_aritmetica
    elif str(letra).upper() == 'P':
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return 'A média é : %.1f' % media_ponderada

    return 'Letra Inválida!'

nota1 = float(input('Nota 1 :'))
nota2 = float(input('Nota 2 :'))
nota3 = float(input('Nota 3 :'))
letra = str(input('Letra :'))

print(f'\n{calculo(nota1, nota2, nota3, letra)}')