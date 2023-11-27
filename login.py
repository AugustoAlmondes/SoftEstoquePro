from pessoa import Pessoa
from cadastro import Cadastro

class Login:
    def __init__(self):
        self.cad = Cadastro
        self.lista = Cadastro._lista_pessoas
        
    # def buscar_usuario(self,senha,cpf):
    #     for usuario in self.lista:
    #         if usuario.cpf == cpf and usuario.senha == senha:
    #             return True        
    #     return False
    
def __str__(self):
    return f"Nome: {self.nome}, Endereço: {self.endereco}, CPF: {self.cpf}, Data de Nascimento: {self.nascimento}, Senha: {self.senha}"