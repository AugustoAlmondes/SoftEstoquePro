import mysql.connector as mysql

class Produto:
    """
        Classe que representa um produto.

        Attributes
        ----------
        produto : str
            Nome do produto.
        preco : float
            Preço do produto.
        fornecedor : str
            Nome do fornecedor do produto.
        data_compra : str
            Data da compra do produto.

        Methods
        -------
        __init__(produto, preco, fornecedor, data_compra)
            Inicializa a classe Produto.
    """


    def __init__(self,produto,preco,fornecedor,data_compra):
        """
            Inicializa a classe Produto.

            Parameters
            ----------
            produto : str
                Nome do produto.
            preco : float
                Preço do produto.
            fornecedor : str
                Nome do fornecedor do produto.
            data_compra : str
                Data da compra do produto.
        """

        self.produto = produto
        self.preco = preco
        self.fornecedor = fornecedor
        self.data_compra = data_compra
    
