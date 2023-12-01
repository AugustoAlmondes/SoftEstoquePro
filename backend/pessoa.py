class Pessoa:
    def __init__(self,cpf,nome, endereco, nascimento,senha,usuario):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.nascimento = nascimento
        self.senha = senha
        self.usuario = usuario
        
def __str__(self):
    return f"Nome: {self.nome}, Endereço: {self.endereco}, CPF: {self.cpf}, Data de Nascimento: {self.nascimento}, Senha: {self.senha}"