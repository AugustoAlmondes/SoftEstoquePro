from pessoa import Pessoa
import mysql.connector as mysql

class Cadastro:
    
    __slots__ = ['mydb','mycursor','_lista_pessoas']

    def __init__(self):
        self._lista_pessoas = []
        self.mydb = self.conectar()
        self.mycursor = self.mydb.cursor()

    def remover_produto(self,produto_remover):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        sql = f'DELETE FROM produtos WHERE id = {produto_remover};'
        print(sql)
        mycursor.execute(sql)       
        print('executou')        
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        print('executou')        
        mycursor.close()
        print('executou')        
        mydb.close()
        print('executou')
        
        return True  

    def cadastra_ususario(self,cpf,nome,endereco,nascimento,senha,usuario):
        
        if (self.busca(cpf,'usuarios','cpf')):
            print('entrou')
            mydb = self.conectar()
            mycursor = mydb.cursor()
            
            # banco_dados = self.verificar_banco_dados(usuario)
            
            sql = f'INSERT INTO usuarios (nome, endereco, cpf, nascimento, senha, usuario) VALUES ("{nome}", "{endereco}","{cpf}", "{nascimento}", "{senha}", "{usuario}")'
            
            mycursor.execute(sql)
            
            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        else:
            print("retornou falso")
            return False
        
    # def busca_login(self,dado,parametro_busca):
    #     mydb = self.conectar()
    #     mycursor = self.mydb.cursor()
        
    #     # banco_dados = self.verificar_banco_dados(usuario)
    #     # print("O banco de dados eh: ",usuarios)
        
    #     sql = f'SELECT * from usuarios where {parametro_busca} = "{dado}";'
    #     # val = parametro_busca
        
    #     mycursor.execute(sql)
    #     result = mycursor.fetchall()
        
    #     # nome, endereco = result[0][2], result[0][3]
    #     # mydb.commit()
    #     mycursor.close()
    #     mydb.close()
    #     # return result
    #     if len(result) != 0:
    #         return True
    #     else:
    #         return False
    
    def busca(self,dado,tabela,parametro_busca):
        mydb = self.conectar()
        mycursor = self.mydb.cursor()
        
        # banco_dados = self.verificar_banco_dados(usuario)
        # print("O banco de dados eh: ",banco_dados)
        
        sql = f'SELECT * from {tabela} where {parametro_busca} = "{dado}";'
        print(sql)
        # val = parametro_busca
        
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        # nome, endereco = result[0][2], result[0][3]
        # mydb.commit()
        mycursor.close()
        mydb.close()
        # return result
        if len(result) == 0:
            print('Não existe na tabela')
            return True
        else:
            print('Existe na tabela')
            return False
    
    def buscar_usuario(self,cpf,senha):
        # banco_dados = 'usuarios'
        # # banco_dados = self.verificar_banco_dados(usuario)
        
        # print('Banco retornado',banco_dados)
        if not(self.busca(cpf,'usuarios',"cpf")):
            print('achou')
            sql = f'SELECT * from usuarios where cpf = "{cpf}" and senha = "{senha}";'
            mydb = self.conectar()
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(result)
            
            if len(result) > 0:
                return True
            else:
                return False
        else:
            return False

    
    def conectar(self):
        conectar = mysql.connect(
        host="localhost",
        user="root",
        password="play2233",
        database="POO2"
        )

        return conectar
    
    def procurar_dado_especifico(self,coluna,tabela,parametro_busca,dado):
        
        result = None
        mydb = self.conectar()
        mycursor = self.mydb.cursor()
        
        # sql = f'SELECT {coluna} FROM administrador where {parametro_busca} = "{dado}" UNION SELECT usuario FROM entregador where {parametro_busca} = "{dado}" UNION SELECT usuario FROM fornecedor where {parametro_busca} = "{dado}" UNION SELECT usuario FROM funcionario where {parametro_busca} = "{dado}";'
        sql = f'SELECT {coluna} from {tabela} where {parametro_busca} = "{dado}"'
        
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        # nome, endereco = result[0][2], result[0][3]
        # mydb.commit()
        mycursor.close()
        mydb.close()
        print('exibindo result:',result)
        if result:
            return(result[0][0])
        else:
            return None
    
    # def verificar_banco_dados(self,usuario):
    #     banco_dados = ''
        
    #     if usuario == 'Administrador':
    #         print('é administrador')
    #         # sql = "INSERT INTO administrador (nome, endereco, cpf, nascimento, senha, usuario) VALUES (%s, %s, %s,%s, %s, %s)"
    #         # val = (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento, pessoa.senha, pessoa.usuario)
    #         # val = ("Augsuto", "rua liz", "2020202", "121212", "joaoo43434", "Administrador")
    #         banco_dados = 'administrador'

    #     elif usuario == 'Entregador':
    #         print('é entregador')
    #         # sql = "INSERT INTO entregador (nome, endereco, cpf, nascimento, senha, usuario) VALUES (%s, %s, %s,%s, %s, %s)"
    #         # val = (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento, pessoa.senha, pessoa.usuario)
    #         # val = ("Augsuto", "rua liz", "2020202", "121212", "joaoo43434", "Administrador")
    #         banco_dados = 'entregador'

    #     elif usuario == 'Funcionario':
    #         print('é funcionario')
    #         # sql = "INSERT INTO cliente (nome, endereco, cpf, nascimento, senha, usuario) VALUES (%s, %s, %s,%s, %s, %s)"
    #         # val = (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento, pessoa.senha, pessoa.usuario)
    #         # val = ("Augsuto", "rua liz", "2020202", "121212", "joaoo43434", "Administrador")
    #         banco_dados = 'funcionario'

    #     elif usuario == 'Fornecedor':
    #         print('é fornecedor')
    #         # sql = "INSERT INTO fornecedor (nome, endereco, cpf, nascimento, senha, usuario) VALUES (%s, %s, %s,%s, %s, %s)"
    #         # val = (pessoa.nome, pessoa.endereco, pessoa.cpf, pessoa.nascimento, pessoa.senha, pessoa.usuario)
    #         # val = ("Augsuto", "rua liz", "2020202", "121212", "joaoo43434", "Administrador")
    #         banco_dados = 'fornecedor'
                
    #     return banco_dados
    
    def cadastra_produto(self, info_produto):
        
        if (self.busca(info_produto.produto,'produtos','produto')):
            print('entrou')
            mydb = self.conectar()
            mycursor = mydb.cursor()
            
            # banco_dados = self.verificar_banco_dados(usuario)
            
            sql = f'insert into produtos (produto, preco, fornecedor, dataCompra) values ("{info_produto.produto}","{info_produto.preco}" , "{info_produto.fornecedor}", "{info_produto.data_compra}")'
            # sql = f'insert into produtos (produto, preco, fornecedor, dataCompra) values ("arroz",17.00,"carvalho","17/03");'
            mycursor.execute(sql)
        
            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        else:
            mydb.commit()
            mycursor.close()
            mydb.close()
            print("retornou falso")
            return False