"""

POO - Atributos

Atributos - Representam as caracteristicas do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

"""

# Classe com Atributos de Instância Público
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def get_email(self):
        return self.__email


a = Acesso.get_email()
