# from pessoa import Pessoa
import mysql.connector as mysql
import bcrypt
class Cadastro:



    def __init__(self):
        self.mydb = self.conectar()
        self.mycursor = self.mydb.cursor()



    def conectar(self):
        conectar = mysql.connect(
        host="localhost",
        user="root",
        password="play2233",
        database="POO2"
        )

        return conectar



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



# ------------------------------------------------------------
# ------------------------USUARIO-----------------------------
    def Login(self,cpf,senha, usuario):
        if not(self.busca(cpf,'usuarios',"cpf")):
            
            # senha_codificada = senha.encode('utf-8')
            sql = f'SELECT * from usuarios where usuario = "{usuario}" and cpf = "{cpf}"'
            print(sql)
            mydb = self.conectar()
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()
            
            print(senha ,'do tipo',type(senha.encode('utf-8')))
            # print(senha_codificada)
            print(result[0][5], 'do tipo', type(result[0][5].encode('utf-8')))
            
            senha_codificada = str(senha)
            result_codificado = str(result[0][5])
            senha_codificada = senha_codificada.encode('utf-8')
            # result_codificado = result_codificado.encode('utf-8')
            result_codificado = eval(result_codificado)
            print(senha_codificada, result_codificado)
            
            if(cpf == result[0][3] and bcrypt.checkpw(senha_codificada, result_codificado)):
                return True
            else:
                return False
        else:
            return False



    def buscar_usuario(self,cpf,senha):
        
        if not(self.busca(cpf,'usuarios',"cpf")):
            print('achou')
            senha_codificada = senha.encode('utf-8')  # Codificar a senha para bytes
            hashed = bcrypt.hashpw(senha_codificada, bcrypt.gensalt())
            sql = f'SELECT * from usuarios where cpf = "{cpf}" and senha = "{hashed}";'
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
        # print("____Entrou____")
        mydb = self.conectar()
        mycursor = mydb.cursor()
        print(usuario)

        sql = f'SELECT id,nome,endereco,cpf,nascimento,usuario FROM usuarios where usuario = \'{usuario}\''

        mycursor.execute(sql)
        lista_usuario = mycursor.fetchall()

        mydb.close()
        print("retornou")
        return lista_usuario



    def RemoverUsuario(self,usuario,id):
        try:
            
            mydb = self.conectar()
            mycursor = mydb.cursor()

            sql = f'DELETE FROM usuarios WHERE usuario = "{usuario}" and nome = "{id}";'
            print(sql)
            mycursor.execute(sql)
            # nome, endereco = result[0][2], result[0][3]
            mydb.commit()
            mycursor.close()
            mydb.close()
            
            return True
        except:
            return False


    def DadosUsuario(self,usuario,nome):
        try:
            print("entrou na busca")
            result = None
            mydb = self.conectar()
            mycursor = self.mydb.cursor()

            sql = f'SELECT id, nome, endereco, cpf, nascimento, usuario from usuarios where usuario = "{usuario}" and nome = "{nome}";'
            print(sql)
            mycursor.execute(sql)
            result = mycursor.fetchall()

            mydb.close()
            print("RETORNOU OS DADOS")
            return result
        except:
            return False



# ------------------------------------------------------------
# ------------------------PRODUTO-----------------------------



    def ListarProdutos(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM estoque")
        lista_produtos = mycursor.fetchall()
        
        mydb.close()
        return lista_produtos



    def cadastra_produto(self, produto, quantidade,data_entrada, preco_compra,preco_venda, fornecedor):
        
        print("Entrou no cadastro_produto")
        
        if (self.busca(produto,'Estoque','produto')):
            print('entrou')
            mydb = self.conectar()
            mycursor = mydb.cursor()

            # banco_dados = self.verificar_banco_dados(usuario)

            sql = f'INSERT INTO Estoque (produto, quantidade, data_entrada, preco_compra, preco_venda, fornecedor) values ("{produto}","{quantidade}" ,"{data_entrada}", "{preco_compra}","{preco_venda}", "{fornecedor}")'
            print(sql)
            # sql = f'insert into produtos (produto, preco, fornecedor, dataCompra) values ("arroz",17.00,"carvalho","17/03");'
            mycursor.execute(sql)

            mydb.commit()
            mycursor.close()
            mydb.close()
            return True
        
        else:
            return False



    def remover_produto(self,id_entrega):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'DELETE FROM Estoque WHERE id = {id_entrega};'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()

        return True



    def RemoverProdutoZerado(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'SET SQL_SAFE_UPDATES = 0;'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'DELETE FROM Estoque WHERE quantidade = 0;'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        return True
# ------------------------------------------------------------
# ------------------------HISTÓRICO---------------------------



    def AdicionarHistorico(self,mensagem, data):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        sql = f'INSERT INTO Historico (DescricaoOperacao,DataOperacao) VALUES ("{mensagem}","{data}")'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        return True



    def ExibirHistorico(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM historico")
        historico = mycursor.fetchall()
        
        mydb.close()
        return historico



# ------------------------------------------------------------
# --------------------------VENDAS----------------------------



    def AdicionarVenda(self,produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'INSERT INTO Vendas (produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda) VALUES ("{produto}", "{quantidade}", "{preco_unitario}", "{total}", "{cliente}", "{responsavel_venda}", "{data_venda}")'
        print("Entrou aqui")
        mycursor.execute(sql)       

        mydb.commit()
        mycursor.close()
        mydb.close()

        mydb = self.conectar()
        mycursor = mydb.cursor()

        # print(produto)
        
        sql = f'UPDATE Estoque SET quantidade = quantidade - {quantidade} WHERE id = {produto};'
        print(sql)
        mycursor.execute(sql)

        mydb.commit()
        mycursor.close()
        mydb.close()

        return True



    def BuscarIdVenda(self,produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'SELECT id FROM Vendas WHERE produto = {produto} and quantidade = {quantidade} and preco_unitario = {preco_unitario} and total = {total} and cliente = "{cliente}" and responsavel_venda = "{responsavel_venda}" and data_venda = "{data_venda}";'
        print(sql)
        mycursor.execute(sql)       

        result = mycursor.fetchall()
        print(result)

        mydb.close()
        return result



    def CadastrarEntrega(self,id_venda,cliente,num_casa, bairro, rua,data):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        sql = f'INSERT INTO Entrega (venda_id, cliente, num_casa, bairro, rua, data_entrega) VALUES ({id_venda},"{cliente}","{num_casa}","{bairro}","{rua}","{data}");'
        print(sql)
        mycursor.execute(sql)       
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        
        return True



    def ExibirEntregas(self):
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM Entrega")
        entrega = mycursor.fetchall()
        
        mydb.close()
        return entrega



    def FinalizarEntrega(self,produto_remover):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'DELETE FROM Estoque WHERE id = {produto_remover};'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()

        return True



    def FinalizarEntrega(self,id_entrega):
        mydb = self.conectar()
        mycursor = mydb.cursor()

        sql = f'DELETE FROM Entrega WHERE id = {id_entrega};'
        print(sql)
        mycursor.execute(sql)       
        # nome, endereco = result[0][2], result[0][3]
        mydb.commit()
        mycursor.close()
        mydb.close()

        return True