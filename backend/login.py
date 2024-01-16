from pessoa import Pessoa
from cadastro import Cadastro

class Login:
    """
        Classe responsável por gerenciar o processo de login.

        Attributes
        ----------
        cad : Cadastro
            Instância da classe Cadastro para acesso a funcionalidades relacionadas a usuários.
        lista : list
            Lista de pessoas cadastradas.

        Methods
        -------
        buscar_usuario(senha, cpf)
            Verifica se um usuário com a senha e CPF fornecidos existe na lista de pessoas cadastradas.
        __str__()
            Retorna uma representação em string da instância.
    """ 
    
    
    def __init__(self):
        """
            Inicializa a classe Login.

            Parameters
            ----------
            cadastro : Cadastro
                Instância da classe Cadastro para acesso a funcionalidades relacionadas a usuários.
        """
        
        self.cad = Cadastro
        self.lista = Cadastro._lista_pessoas
        
    # def buscar_usuario(self,senha,cpf):
    #     for usuario in self.lista:
    #         if usuario.cpf == cpf and usuario.senha == senha:
    #             return True        
    #     return False
    
def __str__(self):
    return f"Nome: {self.nome}, Endereço: {self.endereco}, CPF: {self.cpf}, Data de Nascimento: {self.nascimento}, Senha: {self.senha}"