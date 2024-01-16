class Pessoa:
    """
        Classe que representa uma pessoa.

        Attributes
        ----------
        cpf : str
            CPF da pessoa.
        nome : str
            Nome da pessoa.
        endereco : str
            Endereço da pessoa.
        nascimento : str
            Data de nascimento da pessoa.
        senha : str
            Senha da pessoa.
        usuario : str
            Nome de usuário da pessoa.

        Methods
        -------
        __str__()
            Retorna uma representação em string da instância.
    """
    
    
    def __init__(self,cpf,nome, endereco, nascimento,senha,usuario):
        """
            Inicializa a classe Pessoa.

            Parameters
            ----------
            cpf : str
                CPF da pessoa.
            nome : str
                Nome da pessoa.
            endereco : str
                Endereço da pessoa.
            nascimento : str
                Data de nascimento da pessoa.
            senha : str
                Senha da pessoa.
            usuario : str
                Nome de usuário da pessoa.
        """
        
        
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.nascimento = nascimento
        self.senha = senha
        self.usuario = usuario
        
def __str__(self):
    """
        Retorna uma representação em string da instância.

        Returns
        -------
        str
            Representação em string da instância.
    """

    return f"Nome: {self.nome}, Endereço: {self.endereco}, CPF: {self.cpf}, Data de Nascimento: {self.nascimento}, Senha: {self.senha}"