string = '01234567890123456789012345678901234567890123456789'
n = 10
for i in range(0, len(string), n):
    print(string[i:i+n], end='.')