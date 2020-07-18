carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 40))
carrinho.append(('Produto 3', 50))

total = []
for i in carrinho:
    total.append(i[1])

print(total)
print(sum(total))