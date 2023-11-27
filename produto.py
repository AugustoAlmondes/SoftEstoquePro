import mysql.connector as mysql

class Produto:
    
    def __init__(self,produto,preco,fornecedor,data_compra):
        self.produto = produto
        self.preco = preco
        self.fornecedor = fornecedor
        self.data_compra = data_compra
    
