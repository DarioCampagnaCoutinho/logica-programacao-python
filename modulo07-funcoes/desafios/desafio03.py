def e_par(x):
    return x % 2 == 0


def e_par_ou_impar(x):
    if e_par(x):
        return 'par'
    else:
        return 'impar'


print(e_par_ou_impar(6))
print(e_par_ou_impar(9))