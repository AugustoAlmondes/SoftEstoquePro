# from pessoa import Pessoa
import mysql.connector as mysql

class Cadastro:



    def __init__(self):
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
        print("entrou no cadastrar_usuario")
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



    def busca(self,dado,tabela,parametro_busca):
        mydb = self.conectar()
        mycursor = self.mydb.cursor()

        sql = f'SELECT * from {tabela} where {parametro_busca} = "{dado}";'
        print(sql)
        
        mycursor.execute(sql)
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        if len(result) == 0:
            print('Não existe na tabela')
            return True
        else:
            print('Existe na tabela')
            return False



    def buscar_usuario(self,cpf,senha):
        
        if not(self.busca(cpf,'usuarios',"cpf")):
            print('achou')
            sql = f'SELECT * from usuarios where cpf = "{cpf}" and senha = "{senha}";'
            mydb = self.conectar()
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()
            # print(result)
            
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
        # print('exibindo result:',result)
        if result:
            return(result[0][0])
        else:
            return None



    def buscar_todos_dados(self,banco,parametro_busca,codigo):
        print("entrou na busca")
        result = None
        mydb = self.conectar()
        mycursor = self.mydb.cursor()

        sql = f'SELECT * from {banco} where {parametro_busca} = {codigo};'

        mycursor.execute(sql)
        result = mycursor.fetchall()

        mydb.close()
        print("RETORNOU OS DADOS")
        return result



    def ListarUsuario(self,usuario):
        print("____Entrou____")
        mydb = self.conectar()
        mycursor = mydb.cursor()
        print(usuario)

        sql = f'SELECT id,nome,endereco,cpf,nascimento,usuario FROM usuarios where usuario = \'{usuario}\''

        mycursor.execute(sql)
        lista_usuario = mycursor.fetchall()

        mydb.close()
        print("retornou")
        return lista_usuario



    def ListarProdutos(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM estoque")
        lista_produtos = mycursor.fetchall()
        
        mydb.close()
        return lista_produtos



    def cadastra_produto(self, produto, preco, fornecedor, data_compra):
        
        print("Entrou no cadastro_produto")
        
        if (self.busca(produto,'produtos','produto')):
            print('entrou')
            mydb = self.conectar()
            mycursor = mydb.cursor()
            
            # banco_dados = self.verificar_banco_dados(usuario)
            
            sql = f'insert into produtos (produto, preco, fornecedor, dataCompra) values ("{produto}","{preco}" , "{fornecedor}", "{data_compra}")'
            # sql = f'insert into produtos (produto, preco, fornecedor, dataCompra) values ("arroz",17.00,"carvalho","17/03");'
            mycursor.execute(sql)
        
            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        
        else:
            return False