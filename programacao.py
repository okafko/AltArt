class Cadastro:
    def __init__ (self, nome, email, telefone, endereco, senha, confirmarsenha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.__senha = senha
        self.__confirmarsenha = confirmarsenha