string = '01234567890123456789012345678901234567890123456789'
n = 10
serp = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(serp)
print(serp)
print(retorno)