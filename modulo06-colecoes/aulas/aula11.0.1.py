clientes = {
    'cliente1': {
        'nome': 'Dario',
        'sobreNome': 'Campagna',
    },
    'cliente2': {
        'nome': 'Darius',
        'sobreNome': 'Coutinho',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo : {clientes_k.upper()}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k}={dados_v}')