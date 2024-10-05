# from pessoa import Pessoa
import mysql.connector as mysql
import bcrypt
class Cadastro:
    
    """
        Classe que gerencia operações relacionadas ao banco de dados, como cadastro, busca, remoção e outras.

        Attributes
        ----------
        mydb : mysql.connector.connection.MySQLConnection
            Conexão com o banco de dados.
        mycursor : mysql.connector.cursor.MySQLCursor
            Cursor para executar comandos SQL.

        Methods
        -------
        conectar()
            Estabelece a conexão com o banco de dados.
        busca(dado, tabela, parametro_busca)
            Realiza uma busca no banco de dados.
        procurar_dado_especifico(coluna, tabela, parametro_busca, dado)
            Procura um dado específico em uma coluna da tabela.
        Login(cpf, senha, usuario)
            Realiza o login verificando CPF, senha e usuário.
        buscar_usuario(cpf, senha)
            Busca um usuário no banco de dados.
        cadastra_ususario(cpf, nome, endereco, nascimento, senha, usuario)
            Cadastra um novo usuário no banco de dados.
        buscar_todos_dados(banco, parametro_busca, codigo)
            Busca todos os dados de uma tabela com base em um parâmetro.
        ListarUsuario(usuario)
            Lista informações de um usuário.
        RemoverUsuario(usuario, id)
            Remove um usuário do banco de dados.
        DadosUsuario(usuario, nome)
            Busca dados específicos de um usuário.
        ListarProdutos()
            Lista todos os produtos no estoque.
        cadastra_produto(produto, quantidade, data_entrada, preco_compra, preco_venda, fornecedor)
            Cadastra um novo produto no estoque.
        remover_produto(id_entrega)
            Remove um produto do estoque com base no ID.
        RemoverProdutoZerado()
            Remove produtos do estoque com quantidade zero.
        AdicionarHistorico(mensagem, data)
            Adiciona uma entrada no histórico.
        ExibirHistorico()
            Exibe todo o histórico de operações.
        AdicionarVenda(produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda)
            Adiciona uma nova venda ao banco de dados.
        BuscarIdVenda(produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda)
            Busca o ID de uma venda com base nos parâmetros fornecidos.
        CadastrarEntrega(id_venda, cliente, num_casa, bairro, rua, data)
            Cadastra uma entrega associada a uma venda.
        ExibirEntregas()
            Exibe todas as entregas cadastradas.
        FinalizarEntrega(id_entrega)
            Finaliza uma entrega com base no ID.
    """


    def __init__(self):
        self.mydb = self.conectar()
        self.mycursor = self.mydb.cursor()



    def conectar(self):
        """
        Estabelece a conexão com o banco de dados.

        Returns
        -------
        mysql.connector.connection.MySQLConnection
            Conexão com o banco de dados.
        """
        
        conectar = mysql.connect(
        host="localhost",
        user="root",
        password="suasenha",
        database="suabasededados"
        )

        return conectar



    def busca(self,dado,tabela,parametro_busca):
        """
            Realiza uma busca no banco de dados.

            Parameters
            ----------
            dado : str
                Dado a ser buscado.
            tabela : str
                Tabela onde a busca será realizada.
            parametro_busca : str
                Coluna onde o dado será buscado.

            Returns
            -------
            bool
                True se o dado não for encontrado, False se encontrado.
        """
        
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
        """
            Procura um dado específico em uma coluna da tabela.

            Parameters
            ----------
            coluna : str
                Coluna onde o dado será procurado.
            tabela : str
                Tabela onde a busca será realizada.
            parametro_busca : str
                Coluna onde a busca será realizada.
            dado : str
                Dado a ser procurado.

            Returns
            -------
            str or None
                Valor encontrado na busca ou None se não encontrado.
        
        """
        
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
        """
            Realiza o login verificando CPF, senha e usuário.

            Parameters
            ----------
            cpf : str
                CPF do usuário.
            senha : str
                Senha do usuário.
            usuario : str
                Nome de usuário.

            Returns
            -------
            bool
                True se o login for bem-sucedido, False caso contrário.
        """
        
        
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
        """
            Busca um usuário no banco de dados.

            Parameters
            ----------
            cpf : str
                CPF do usuário.
            senha : str
                Senha do usuário.

            Returns
            -------
            bool
                True se o usuário for encontrado, False caso contrário.
        """


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
        """
            Cadastra um novo usuário no banco de dados.

            Parameters
            ----------
            cpf : str
                CPF do usuário.
            nome : str
                Nome do usuário.
            endereco : str
                Endereço do usuário.
            nascimento : str
                Data de nascimento do usuário.
            senha : str
                Senha do usuário.
            usuario : str
                Nome de usuário.

            Returns
            -------
            bool
                True se o cadastro for bem-sucedido, False caso contrário.
        """
        
        
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
        """
            Busca todos os dados de uma tabela com base em um parâmetro.

            Parameters
            ----------
            banco : str
                Tabela onde a busca será realizada.
            parametro_busca : str
                Coluna onde a busca será realizada.
            codigo : str
                Valor a ser buscado.

            Returns
            -------
            list
                Lista com os resultados da busca.
        """
        
        
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
        """
            Lista informações de um usuário.

            Parameters
            ----------
            usuario : str
                Nome de usuário.

            Returns
            -------
            list
                Lista com informações do usuário.
        """
        
        
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
        """
            Remove um usuário do banco de dados.

            Parameters
            ----------
            usuario : str
                Nome de usuário.
            id : str
                ID do usuário a ser removido.

            Returns
            -------
            bool
                True se a remoção for bem-sucedida, False caso contrário.
        """
        
        
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
        """
            Busca dados específicos de um usuário.

            Parameters
            ----------
            usuario : str
                Nome de usuário.
            nome : str
                Nome do usuário a ser buscado.

            Returns
            -------
            list
                Lista com os dados do usuário.
        """
        
        
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
        """
            Lista todos os produtos no estoque.

            Returns
            -------
            list
                Lista com informações dos produtos.
        """ 
        
        
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM estoque")
        lista_produtos = mycursor.fetchall()
        
        mydb.close()
        return lista_produtos



    def cadastra_produto(self, produto, quantidade,data_entrada, preco_compra,preco_venda, fornecedor):
        """
            Cadastra um novo produto no estoque.

            Parameters
            ----------
            produto : str
                Nome do produto.
            quantidade : int
                Quantidade em estoque.
            data_entrada : str
                Data de entrada do produto no estoque.
            preco_compra : float
                Preço de compra do produto.
            preco_venda : float
                Preço de venda do produto.
            fornecedor : str
                Nome do fornecedor.

            Returns
            -------
            bool
                True se o cadastro for bem-sucedido, False caso contrário.
        """


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
        """
            Remove um produto do estoque com base no ID de entrega.

            Parameters
            ----------
            id_entrega : int
                ID de entrega associado ao produto no estoque.

            Returns
            -------
            bool
                True se a remoção for bem-sucedida, False caso contrário.
        """
        
        
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
        """
            Remove produtos do estoque que possuem quantidade zero.

            Returns
            -------
            bool
                True se a remoção for bem-sucedida, False caso contrário.
        """
        
        
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
        """
            Adiciona uma entrada ao histórico de operações no banco de dados.

            Parameters
            ----------
            mensagem : str
                Descrição da operação realizada.
            data : str
                Data da operação.

            Returns
            -------
            bool
                True se a adição ao histórico for bem-sucedida, False caso contrário.
        """
        
        
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
        """
            Exibe todo o histórico de operações.

            Returns
            -------
            list of tuples
                Lista contendo todas as entradas no histórico, representadas como tuplas.
        """
        
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM historico")
        historico = mycursor.fetchall()
        
        mydb.close()
        return historico



# ------------------------------------------------------------
# --------------------------VENDAS----------------------------



    def AdicionarVenda(self,produto, quantidade, preco_unitario, total, cliente, responsavel_venda, data_venda):
        """
            Adiciona uma nova venda ao banco de dados.

            Parameters
            ----------
            produto : str
                Nome do produto vendido.
            quantidade : int
                Quantidade vendida.
            preco_unitario : float
                Preço unitário do produto.
            total : float
                Valor total da venda.
            cliente : str
                Nome do cliente.
            responsavel_venda : str
                Nome do responsável pela venda.
            data_venda : str
                Data da venda.

            Returns
            -------
            bool
                True se a adição da venda for bem-sucedida, False caso contrário.
        """
        
        
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
        """
            Busca o ID de uma venda específica no banco de dados.

            Parameters
            ----------
            produto : str
                Nome do produto vendido.
            quantidade : int
                Quantidade vendida.
            preco_unitario : float
                Preço unitário do produto.
            total : float
                Valor total da venda.
            cliente : str
                Nome do cliente.
            responsavel_venda : str
                Nome do responsável pela venda.
            data_venda : str
                Data da venda.

            Returns
            -------
            list of tuples
                Lista contendo os IDs das vendas que correspondem aos parâmetros fornecidos.
        """
        
        
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
        """
            Cadastra uma entrega associada a uma venda.

            Parameters
            ----------
            id_venda : int
                ID da venda associada à entrega.
            cliente : str
                Nome do cliente.
            num_casa : str
                Número da casa para entrega.
            bairro : str
                Bairro da entrega.
            rua : str
                Rua da entrega.
            data : str
                Data da entrega.

            Returns
            -------
            bool
                True se o cadastro da entrega for bem-sucedido, False caso contrário.
        """
        
        
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
        """
            Exibe todas as entregas cadastradas.

            Returns
            -------
            list of tuples
                Lista contendo todas as entradas de entregas, representadas como tuplas.
        """
        
        
        mydb = self.conectar()
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT * FROM Entrega")
        entrega = mycursor.fetchall()
        
        mydb.close()
        return entrega



    def FinalizarEntrega(self,produto_remover):
        """
            Finaliza uma entrega removendo o produto do estoque.

            Parameters
            ----------
            produto_remover : int
                ID do produto a ser removido do estoque.

            Returns
            -------
            bool
                True se a finalização for bem-sucedida, False caso contrário.
        """
       

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
        """
            Finaliza uma entrega removendo a entrada de entrega no banco de dados.

            Parameters
            ----------
            id_entrega : int
                ID da entrega a ser finalizada.

            Returns
            -------
            bool
                True se a finalização for bem-sucedida, False caso contrário.
        """
        
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
