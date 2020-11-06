class Aluno:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return '\nAluno:' + self.nome + '\nEndereço:' + self.endereco + '\nEmail:' + self.email

lista = []
while True:
    print('Escolha uma opção')
    print('<1> - Cadastrar')
    print('<2> - Listar')
    print('<3> - Sair')
    escolha = input('Digite uma opção e pressione <ENTER>')
    if escolha == '1':
        nome = input('Digite um Nome : ')
        endereco = input('Digite um Endereço :')
        email = input('Digite um email : ')
        aluno = Aluno(nome, endereco, email)
        lista.append(aluno)
    elif escolha == '2':
        for i in lista:
            print(i)
            input('Digite <ENTER> para continuar!')
    elif escolha == '3':
        break