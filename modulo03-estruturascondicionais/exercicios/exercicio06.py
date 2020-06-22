codigo = int(input('Digite o código do produto = '))
quantidade = int(input('Digite a quantidade de itens = '))

if codigo == 100:
    preco = 4.00
    cq = 'Cachorro Quente'
    total = preco * quantidade
    print('O preço de um {} é = {} R$'.format(cq, preco))
    print('O total do pedido é = {} R$'.format(total))
elif codigo == 101:
    preco = 2.00
    bs = 'Bauru Simples'
    total = preco * quantidade
    print('O preço de um {} é = {} R$'.format(bs, preco))
    print('O total do pedido é = {} R$'.format(total))
else:
    print('Opção Inválida, Execute o programa novamente')


