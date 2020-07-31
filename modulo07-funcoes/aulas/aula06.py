a = lambda x, y: x * y

print(a(2, 4))

lista = [
    ['P1', 10],
    ['P2', 7],
    ['P3', 20],
    ['P4', 14],
    ['P5', 2],
]

print(sorted(lista, key=lambda i:i[1]))
print(sorted(lista, key=lambda i:i[1], reverse=True))