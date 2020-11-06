from passlib.hash import pbkdf2_sha512 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Classe: {cls}")
        print(f"Temos {cls.contador} usuário(s) no sistema")

    @classmethod
    def ver(cls):
        print("Teste")

    @staticmethod
    def definicao():
        return "UXR344"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome.strip().title()
        self.__sobrenome = sobrenome.strip().title()
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=2000000, salt_size=28)
        Usuario.contador = self.__id

        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True

        return False

    def __gera_usuario(self):
        return self.__email.split("@")[0]


user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")
user2 = Usuario("Felicity", "Jones", "felicity@gmail.com", "654321")

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f"Senha: {user1._Usuario__senha}")  # Acesso de forma errada de um atributo de classe
print(f"Senha: {user2._Usuario__senha}")  # Acesso de forma errada de um atributo de classe

nome1 = input("Informe o nome: ")
sobrenome1 = input("Informe o sobrenome: ")
email1 = input("Informe o e-mail: ")
senha1 = input("Informe a senha: ")
confirma1 = input("Confirme a senha: ")

while senha1 != confirma1:
    print("\nAs senhas digitadas não são as mesmas, tente novamente!")
    senha1 = input("\nInforme a senha: ")
    confirma1 = input("Confirme a senha: ")

print("\nUsuário criado com sucesso!")

user1 = Usuario(nome1, sobrenome1, email1, senha1)

senha1 = input("\nInforme a senha para acesso: ")

if user1.checa_senha(senha1):
    print("\nAcesso permitido!")
    print(f"Senha do User 1 Criptografada: {user1._Usuario__senha}")  # Acesso errado

else:
    print("\nAcesso negado!")

# Métodos de Classe em Python são conhecidos como métodos estáticos em outras linguagens

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta


# Métodos de Classe

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

print(user._Usuario__gera_usuario())  # Acesso, de forma ruim...


# Métodos Estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario("felicity", "jones", "felicity@gmail.com", "123456")

print(user.contador)

print(user.definicao())

