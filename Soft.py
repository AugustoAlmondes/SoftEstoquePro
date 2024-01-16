import sys
import mysql.connector as mysql
from datetime import date
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from frontend.tela_inicial import *
from frontend.tela_cadastro import *
from frontend.tela_produto import *
from frontend.tela_estoque_funcionario import *
from frontend.tela_login import *
from frontend.tela_bem_vindo import * #ADMINISTRADOR
from frontend.tela_entregador import * #ENTREGADOR
from frontend.tela_funcionario import * #FUNCIONARIO
from frontend.tela_fornecedores import * #FONECEDOR 
from frontend.tela_usuario import * #USUARIO
from frontend.tela_historico import * #HISTORICO
from frontend.tela_vendas import * #VENDAS

from server_cliente import *
from server_servidor import *

# from pessoa import Pessoa
# from cadastro import Cadastro
# from login import Login
# from produto import Produto

class Ui_Main(QtWidgets.QWidget):
    """
        Classe para configurar interface gráfica

        Parameters:
        ----------
        QtWidgets.QWidget
        fundamental para a criação e manipulação de elementos gráficos em uma interface.
    """

    def setupUi(self, Main):
        """
            Configura a interface gráfica da aplicação.

            Parameters:
            ----------
            Main
            Referência à instância principal da aplicação.

        """
        
        
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack2)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack0)
        
        self.tela_bem_vindo = Tela_bem_vindo()
        self.tela_bem_vindo.setupUi(self.stack3)
        
        self.tela_funcionario = Tela_funcionario()
        self.tela_funcionario.setupUi(self.stack4)
        
        self.tela_fornecedores = Tela_fornecedores()
        self.tela_fornecedores.setupUi(self.stack5)
        
        self.tela_entregador = Tela_entregador()
        self.tela_entregador.setupUi(self.stack6)
        
        self.tela_produto = Tela_produto()
        self.tela_produto.setupUi(self.stack7)
        
        self.tela_usuario = Tela_usuario()
        self.tela_usuario.setupUi(self.stack8)
        
        self.tela_historico = Tela_historico()
        self.tela_historico.setupUi(self.stack9)
        
        self.tela_vendas = Tela_vendas()
        self.tela_vendas.setupUi(self.stack10)
        
        self.tela_estoque_funcionario = Tela_produto_funcionario()
        self.tela_estoque_funcionario.setupUi(self.stack11)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)


class Main(QMainWindow, Ui_Main):
    """
        Esta classe representa a janela principal da aplicação.

        Parameters:
        ----------
        QMainWindow : QtWidgets.QMainWindow
        Classe base para a interface principal da janela.

        Ui_Main : Classe de UI gerada
        Classe de UI gerada pelo Qt Designer para a janela principal.

        Attributes:
        ----------
        server : server_cliente
        Uma instância da classe 'server_cliente'.

        dados_produtos : list
        ma lista para armazenar os dados dos produtos.

        usuario : None
        Espaço reservado para os dados do usuário.

        opcao_selecionada : None
        Espaço reservado para a opção selecionada.

        Methods:
        -------
        __init__(self)
            Inicializa a janela principal e configura os componentes de UI.
"""
    
    
    
    def __init__(self):
        """
            Inicializa a classe Main.

            Esta função configura a janela principal da aplicação e conecta os botões às funções correspondentes.

        """
        
        super(Main, self).__init__()
        self.setupUi(self)

        self.server = server_cliente('192.168.18.107',4050)
        self.dados_produtos = []
        self.usuario = None
        
        self.opcao_selecionada = None

        #ADMINISTRADOR
        # self.tela_bem_vindo.pushButton_8.clicked.connect(self.abrirTelaCadastro)
        self.tela_bem_vindo.pushButton_7.clicked.connect(self.abrirTelaProduto)
        self.tela_bem_vindo.pushButton_3.clicked.connect(self.abrirTelaUsuario)
        self.tela_bem_vindo.pushButton_8.clicked.connect(self.abrirTelaHistorico)
        self.tela_bem_vindo.pushButton_2.clicked.connect(self.abrirTelaVendas)

        # funções dos botões da tela principal
        self.tela_inicial.pushButton_3.clicked.connect(self.sair) # funções dos botões da tela principal
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)
        # self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.abrirTelaUsuario)

        self.tela_login.pushButton.clicked.connect(self.botaoLogin)
        # self.tela_login.pushButton_2.clicked.connect(self.abrirTelaCadastro)

        self.tela_bem_vindo.pushButton_6.clicked.connect(self.voltarTelaInicial)
        self.tela_entregador.pushButton_6.clicked.connect(self.voltarTelaInicial)
        self.tela_fornecedores.pushButton_6.clicked.connect(self.voltarTelaInicial)
        self.tela_funcionario.pushButton_6.clicked.connect(self.voltarTelaInicial)

        # TELA PRODUTO
        self.tela_produto.pushButton.clicked.connect(self.botaoCadastrarProduto)
        self.tela_produto.pushButton_2.clicked.connect(self.TelaProdutoFrameListar)
        self.tela_produto.pushButton_2.clicked.connect(self.ListarProdutos)
        self.tela_produto.pushButton_3.clicked.connect(self.TelaProdutoFrameAdicionar)
        self.tela_produto.pushButton_4.clicked.connect(self.TelaProdutoFrameRemover)
        self.tela_produto.pushButton_5.clicked.connect(self.TelaProdutoFrameBuscar)
        self.tela_produto.pushButton_6.clicked.connect(self.abrirTelaBemVindo)
        self.tela_produto.pushButton_7.clicked.connect(self.BuscarProduto)
        self.tela_produto.pushButton_8.clicked.connect(self.botaoRemoverProduto)

        self.tela_estoque_funcionario.pushButton_2.clicked.connect(self.TelaProdutoFrameListarFuncionario)
        self.tela_estoque_funcionario.pushButton_2.clicked.connect(self.ListarProdutosFuncionario)
        self.tela_estoque_funcionario.pushButton_6.clicked.connect(self.AbrirTelaFuncionario)
        self.tela_estoque_funcionario.pushButton_5.clicked.connect(self.TelaProdutoFrameBuscarFuncionario)
        self.tela_estoque_funcionario.pushButton_7.clicked.connect(self.BuscarProdutoFuncionario)

        #TELA USUARIO
        self.tela_usuario.pushButton_2.clicked.connect(self.abrirTelaCadastro)
        self.tela_usuario.pushButton_3.clicked.connect(self.TelaUsuarioTipos)
        self.tela_usuario.pushButton_4.clicked.connect(self.TelaUsuarioRemover)
        self.tela_usuario.pushButton_5.clicked.connect(self.TelaUsuarioBuscar)
        self.tela_usuario.pushButton_6.clicked.connect(self.abrirTelaBemVindo)
        self.tela_usuario.pushButton_7.clicked.connect(self.botaoBuscarUsuario)
        self.tela_usuario.pushButton_27.clicked.connect(self.botaoExibirAdministradores)
        self.tela_usuario.pushButton_28.clicked.connect(self.botaoExibirFuncionario)
        self.tela_usuario.pushButton_29.clicked.connect(self.botaoExibirFornecedor)
        self.tela_usuario.pushButton_30.clicked.connect(self.botaoExibirEntregador)
        self.tela_usuario.pushButton_8.clicked.connect(self.botaoRemoverUsuario)

        #TELA HISTORICO
        self.tela_bem_vindo.pushButton_8.clicked.connect(self.botaoExibirHistorico)
        self.tela_historico.pushButton_6.clicked.connect(self.abrirTelaBemVindo)

        #TELA VENDAS
        self.tela_bem_vindo.pushButton_2.clicked.connect(self.TelaVendasFrameInicial)
        self.tela_vendas.pushButton_6.clicked.connect(self.abrirTelaBemVindo)
        self.tela_vendas.pushButton_2.clicked.connect(self.TelaVendasFrameRealizarVenda)
        self.tela_vendas.pushButton_4.clicked.connect(self.BotaoRealizarVenda)
        self.tela_vendas.pushButton_4.clicked.connect(self.TelaVendasFrameInicial)
        self.tela_vendas.pushButton.clicked.connect(self.AbrirFrameOpcaoVenda)  
        self.tela_vendas.pushButton_5.clicked.connect(self.AbrirTelaVendaEntrega)
        self.tela_vendas.pushButton_7.clicked.connect(self.MostrarDadosTelaVendas)
        self.tela_vendas.pushButton_8.clicked.connect(self.CadastrarEntrega)
        self.tela_vendas.pushButton_9.clicked.connect(self.TelaVendasFrameRealizarVenda)
        self.tela_vendas.pushButton_10.clicked.connect(self.TelaVendasFrameTotal)
        self.tela_vendas.pushButton_14.clicked.connect(self.AbrirFrameEntrega)
        self.tela_vendas.pushButton_11.clicked.connect(self.AbrirFrameEntrega)
        self.tela_vendas.pushButton_12.clicked.connect(self.AbrirFrameEntrega)
        self.tela_vendas.pushButton_20.clicked.connect(self.AbrirFrameEntrega)
        self.tela_vendas.pushButton_15.clicked.connect(self.AbrirFrameListarEntrega)
        self.tela_vendas.pushButton_15.clicked.connect(self.botaoExibirEntregas)
        self.tela_vendas.pushButton_16.clicked.connect(self.AbrirFrameFinalizarEntrega)
        self.tela_vendas.pushButton_17.clicked.connect(self.AbrirFrameBuscarEntrega)
        self.tela_vendas.pushButton_18.clicked.connect(self.botaobuscarEntregaFinalizar)
        self.tela_vendas.pushButton_19.clicked.connect(self.botaoFinalizarEntrega)
        self.tela_vendas.pushButton_21.clicked.connect(self.botaobuscarDadosEntrega)

        #FUNCIONÁRIO
        self.tela_funcionario.pushButton_9.clicked.connect(self.AbrirTelaEstoqueFuncionario)
        self.tela_funcionario.pushButton_2.clicked.connect(self.abrirTelaVendas)
        self.tela_funcionario.pushButton_2.clicked.connect(self.TelaVendasFrameInicial)
        self.tela_funcionario.pushButton_10.clicked.connect(self.abrirTelaHistorico)
        self.tela_funcionario.pushButton_10.clicked.connect(self.botaoExibirHistorico)

    def abrirTelaBemVindo(self):
        """
            Abre a tela inicial com base no tipo de usuário.

            - Se o usuário for Administrador ou Funcionário, abre a tela correspondente com a remoção de produtos zerados do estoque.
            - Se o usuário for Entregador, volta para a tela inicial de login.
            - Se o usuário for Fornecedor, abre a tela correspondente.

        """
        
        if(self.usuario == 'Administrador'):
            self.QtStack.setCurrentIndex(3)
            self.RemoverProdutoZeradoEstoque()
        elif(self.usuario == 'Funcionario'):
            self.QtStack.setCurrentIndex(4)
            self.RemoverProdutoZeradoEstoque()
        if(self.usuario == 'Entregador'):
            self.QtStack.setCurrentIndex(0)
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
        elif(self.usuario == 'Fornecedor'):
            self.QtStack.setCurrentIndex(6)


    def AbrirTelaFuncionario(self):
        """
            Abre a tela correspondente ao Funcionário.

            Se o usuário for Funcionário, abre a tela de Funcionário.
            Se não, volta para a tela inicial de login.

        """
        
        if(self.usuario == 'Funcionario'):
            self.QtStack.setCurrentIndex(4)
        else:
            self.QtStack.setCurrentIndex(0)
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')

    def abrirTelaCadastro(self):
        """
                Abre tela cadastro.

                Utiliza setCurrentIndex(1) para mostrar a página correspondente no QtStack
        
        """
        
        self.QtStack.setCurrentIndex(1)

    def abrirTelaProduto(self):
        """
                Abre tela produto.

                Utiliza setCurrentIndex(7) para mostrar a página correspondente no QtStack
        
        """
        self.QtStack.setCurrentIndex(7)

    def abrirTelaUsuario(self):
        """
                Abre tela usuário.

                Utiliza setCurrentIndex(8) para mostrar a página correspondente no QtStack
        
        """
        
        self.QtStack.setCurrentIndex(8)

    def abrirTelaLogin(self): 
        """
                Abre tela login.

                Utiliza setCurrentIndex(2) para mostrar a página correspondente no QtStack
        
        """
        self.QtStack.setCurrentIndex(2)

    def abrirTelaHistorico(self):
        """
                Abre tela histórico

                Utiliza setCurrentIndex(9) para mostrar a página correspondente no QtStack
        
        """
        
        self.QtStack.setCurrentIndex(9)

    def abrirTelaVendas(self):
        """
            Abre a tela de vendas

            Utiliza setCurrentIndex(10) para mostrar a página correspondente no QtStack
        
        """
        
        self.QtStack.setCurrentIndex(10)

    def TelaProdutoFrameAdicionar(self):
        """
            Abre tela adicionar produto

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de produto
        
        """
        
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page)
        
    def TelaProdutoFrameListar(self):
        """
            Abre tela listar produtos

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de produto
        
        """
        
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_2)
        
    def TelaProdutoFrameBuscar(self):
        """
            Abre tela buscar produto

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de produto.
        
        """
        
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_3)
        
    def TelaProdutoFrameRemover(self):
        """
            Abre tela remover produto

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de produto
        
        """
        
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_4)

    def TelaUsuarioListar(self):
        """
            Abre tela listar usuário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de usuário
        
        """
        
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_2)
        
    def TelaUsuarioRemover(self):
        """
            Abre tela remover usuário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de usuário
        
        """
        
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_4)
        
    def TelaUsuarioBuscar(self):
        """
            Abre tela buscar usuário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de usuário
        
        """
        
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_3)
        
    def TelaUsuarioTipos(self):
        """
            Abre tela tipos de usuário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de usuário
        
        """
        
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page)    

    def AbrirTelaVendaEntrega(self):
        """
            Abre tela entregar venda

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_3)

    def TelaVendasFrameInicial(self):
        """
            Abre tela venda inicial

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_11)

    def TelaVendasFrameRealizarVenda(self):
        """
            Abre tela realizar venda

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
    
    def TelaVendasFrameTotal(self):
        """
            Abre tela total de vendas

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)
    
    def AbrirFrameEntrega(self):
        """
            Abre tela entregas

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_7)
    
    def AbrirFrameBuscarEntrega(self):
        """
            Abre tela buscar entregas

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_10)
    
    def AbrirFrameFinalizarEntrega(self):
        """
            Abre tela finalizar entrega

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """
        
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_9)
    
    def AbrirFrameListarEntrega(self):
        """
            Abre listar entregas

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de vendas
        
        """

        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_8)

    def TelaProdutoFrameListarFuncionario(self):
        """
            Abre listar Funcionário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de estoque funcionário
        
        """
        
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_2)

    def TelaProdutoFrameBuscarFuncionario(self):
        """
            Abre tela Buscar Funcionário

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de estoque funcionário
        
        """
        
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_3)

    def AbrirTelaEstoqueFuncionario(self):
        """
            Abre tela estoque

            Utiliza setCurrentWidget para mostrar a página correspondente no widget PAGINAS da tela de estoque funcionário
        
        """
        
        self.QtStack.setCurrentIndex(11)
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_5)

    def botaoFinalizarEntrega(self):
        """
            Abre finalizar entrega
            Esta função é responsável por finalizar uma entrega, enviando mensagens ao servidor para buscar e concluir a entrega.

        """

        
        codigo = self.tela_vendas.lineEdit_13.text()
        
        if(codigo != ''):
            concatena = f'busca*{codigo}*Entrega*id'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            
            if(result == 'False'):
                concatena = f'FinalizarEntrega*{codigo}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                if(result == 'True'):
                    data = date.today()
                    mensage_hist = f'Entrega de id {codigo} finalizada pelo Usuário {self.usuario}'
                    concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                    self.server.send(concatena.encode())
                    result = self.server.recv(2048)
                    result = result.decode()
                    self.tela_vendas.lineEdit_13.setText('')
                    QMessageBox.information(None,'POOII', 'Entrega finalizada com sucesso')
                else:
                    self.tela_vendas.lineEdit_13.setText('')
                    QMessageBox.information(None,'POOII', 'Algo deu errado')
            else:
                self.tela_vendas.lineEdit_13.setText('')
                QMessageBox.information(None,'POOII', 'A entrga não foi encontrada')
        else:
            self.tela_vendas.lineEdit_13.setText('')
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')


    def botaobuscarEntregaFinalizar(self):
        """
            Busca informações de entrega
            
            Esta função busca informações sobre uma entrega com base no código fornecido e exibe os detalhes na interface gráfica.
        
        """
        
        
        codigo = self.tela_vendas.lineEdit_13.text()
        
        if(codigo != ''):
            concatena = f'busca*{codigo}*Entrega*id'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            
            if(result == 'False'):
                
                concatena = f'buscar_todos_dados*Entrega*id*{codigo}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                result = result.replace('datetime.date','')
                result = eval(result)
                
                self.tela_vendas.tableWidget_5.setRowCount(len(result))
                self.tela_vendas.tableWidget_5.setColumnCount(7)

                for i in range (0, len(result)):
                    for j in range(0,7):
                        self.tela_vendas.tableWidget_5.setItem(i,j,QtWidgets.QTableWidgetItem(str(result[i][j])))
                self.tela_vendas.lineEdit_13.setText('')
            else:
                self.tela_vendas.lineEdit_13.setText('')
                QMessageBox.information(None,'POOII', 'A entrega não foi encontrada')
        else:
            self.tela_vendas.lineEdit_13.setText('')            
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')



    def botaobuscarDadosEntrega(self):
        """
            Esta função busca informações sobre uma entrega com base no código fornecido e exibe os detalhes na interface gráfica.
            
            Além disso, ela busca os dados relacionados à venda associada a essa entrega e os exibe em outra tabela.
        
        """
        
        codigo = self.tela_vendas.lineEdit_14.text()
        
        if(codigo != ''):
            concatena = f'busca*{codigo}*Entrega*id'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            
            if(result == 'False'):
                
                concatena = f'buscar_todos_dados*Entrega*id*{codigo}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                result = result.replace('datetime.date','')
                result = eval(result)
                
                codigo_venda = result[0][1]
                
                self.tela_vendas.tableWidget_6.setRowCount(len(result))
                self.tela_vendas.tableWidget_6.setColumnCount(7)

                for i in range (0, len(result)):
                    for j in range(0,7):
                        self.tela_vendas.tableWidget_6.setItem(i,j,QtWidgets.QTableWidgetItem(str(result[i][j])))
                self.tela_vendas.lineEdit_14.setText('')
                
                concatena = f'buscar_todos_dados*Vendas*id*{codigo_venda}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                print(result)
                
                result = result.replace('datetime.date','').replace('Decimal','')
                result = eval(result)
                
                self.tela_vendas.tableWidget_7.setRowCount(len(result))
                self.tela_vendas.tableWidget_7.setColumnCount(8)

                for i in range (0, len(result)):
                    for j in range(0,8):
                        self.tela_vendas.tableWidget_7.setItem(i,j,QtWidgets.QTableWidgetItem(str(result[i][j])))
                self.tela_vendas.lineEdit_14.setText('')
            else:
                self.tela_vendas.lineEdit_14.setText('')
                QMessageBox.information(None,'POOII', 'A entrega não foi encontrada')
        else:
            self.tela_vendas.lineEdit_14.setText('')
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')



    def botaoExibirEntregas(self):
        """
            Este método solicita ao servidor a exibição de todas as entregas disponíveis e as exibe em uma tabela na interface gráfica.
        
        """
        
        concatena = f'ExibirEntregas'
        self.server.send(concatena.encode())
        entregas = self.server.recv(2048)
        entregas = entregas.decode()
        
        entregas = entregas.replace('datetime.date','')
        entregas = eval(entregas)

        self.tela_vendas.tableWidget_4.setRowCount(len(entregas))
        self.tela_vendas.tableWidget_4.setColumnCount(7)

        for i in range (0, len(entregas)):
            for j in range(0,7):
                self.tela_vendas.tableWidget_4.setItem(i,j,QtWidgets.QTableWidgetItem(str(entregas[i][j])))



    def AbrirFrameOpcaoVenda(self):
        """
            Este método é responsável por abrir o frame de opção de venda na interface gráfica.
            
            Ele também busca e exibe informações sobre o produto selecionado, calcula o total da venda e atualiza a interface.

        """


        self.dados_produtos.append(self.tela_vendas.lineEdit.text()) #CÓDIGO
        self.dados_produtos.append(self.tela_vendas.lineEdit_2.text()) #QUANTIDADE
        self.dados_produtos.append(self.tela_vendas.lineEdit_3.text()) #CLIENTE
        self.dados_produtos.append(self.tela_vendas.lineEdit_4.text()) #FUNCIONARIO
        
        concatena = f'buscar_todos_dados*estoque*id*{self.dados_produtos[0]}'
        self.server.send(concatena.encode())
        result = self.server.recv(2048)
        result = result.decode()

        result = result.replace('Decimal','').replace('datetime.date','')
        result = eval(result)
        preco_unidade = result[0][5]
        total = float(preco_unidade) * int(self.dados_produtos[1])
        total = round(total,2)
        
        self.tela_vendas.lineEdit_8.setText(str(total))
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)



    def MostrarDadosTelaVendas(self):
        """
            Este método busca e exibe os dados do produto na interface gráfica com base no código fornecido.

        """
        
        codigo = self.tela_vendas.lineEdit.text()
        
        if(codigo != ''):
            
            concatena = f'busca*{codigo}*Estoque*id'
            
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            
            if(result == 'False'):
                concatena = f'buscar_todos_dados*Estoque*id*{codigo}'
                
                self.server.send(concatena.encode())
                infor_prod = self.server.recv(2048)
                infor_prod = infor_prod.decode()
                
                infor_prod = infor_prod.replace('Decimal','').replace('datetime.date','')
                infor_prod = eval(infor_prod)

                self.tela_vendas.tableWidget_2.setRowCount(len(infor_prod))
                self.tela_vendas.tableWidget_2.setColumnCount(7)

                for i in range (0, len(infor_prod)):
                    for j in range(0, 7):
                        self.tela_vendas.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(infor_prod[i][j])))
            else:
                QMessageBox.information(None,'POOII', 'ID do produto nao encontrado')
                self.tela_vendas.lineEdit.setText('')
        else:
            QMessageBox.information(None,'POOII', 'O campo do Código deve ser preenchido')



    def CadastrarEntrega(self):
        """
            Realiza o cadastro de uma entrega, verificando a disponibilidade do produto no estoque e a existência do funcionário.

            Obtém os dados da entrega a partir dos campos da interface gráfica.
            Verifica a existência do funcionário no sistema.
            Verifica a existência do produto no estoque.
            Caso tudo esteja correto, adiciona a venda, cadastra a entrega e registra no histórico.

        """
        
        self.dados_produtos.append(self.tela_vendas.lineEdit.text()) #CÓDIGO
        self.dados_produtos.append(self.tela_vendas.lineEdit_2.text()) #QUANTIDADE
        self.dados_produtos.append(self.tela_vendas.lineEdit_3.text()) #CLIENTE
        self.dados_produtos.append(self.tela_vendas.lineEdit_4.text()) #FUNCIONARIO
        
        if not(self.dados_produtos[0] == '' and self.dados_produtos[1] == '' and self.dados_produtos[2] == '' and self.dados_produtos[3] == ''):
            
            concatena = f'DadosUsuario*Funcionario*{self.dados_produtos[3]}'
            self.server.send(concatena.encode())
            verificacao_1 = self.server.recv(2048)
            verificacao_1 = verificacao_1.decode()
            
            concatena = f'DadosUsuario*Administrador*{self.dados_produtos[3]}'
            self.server.send(concatena.encode())
            verificacao_2 = self.server.recv(2048)
            verificacao_2 = verificacao_2.decode()
            
            verificacao_1 = eval(verificacao_1)
            verificacao_2 = eval(verificacao_2)
            
            print(verificacao_1)
            print(verificacao_2)
            
            if(len(verificacao_1) > 0 or len(verificacao_2) > 0):
                concatena = f'busca*{self.dados_produtos[0]}*Estoque*id'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()

                if(result == 'False'):
                    concatena = f'buscar_todos_dados*estoque*id*{self.dados_produtos[0]}'
                    self.server.send(concatena.encode())
                    result = self.server.recv(2048)
                    result = result.decode()

                    result = result.replace('Decimal','').replace('datetime.date','')
                    result = eval(result)
                    
                    try:
                        int(self.dados_produtos[1])
                        if(int(result[0][2]) >= int(self.dados_produtos[1])):
                            preco_unidade = result[0][5]
                            total = float(preco_unidade) * int(self.dados_produtos[1])
                            total = round(total,2)
                            
                            data = date.today()
                            produto = result[0][1]
                            # print(self.dados_produtos)
                            
                            concatena = f'AdicionarVenda*{self.dados_produtos[0]}*{self.dados_produtos[1]}*{preco_unidade}*{total}*{self.dados_produtos[2]}*{self.dados_produtos[3]}*{data}'
                            self.server.send(concatena.encode())
                            result = self.server.recv(2048)
                            result = result.decode()
                            print("Adicionou venda")
                            
                            concatena = f'BuscarIdVenda*{self.dados_produtos[0]}*{self.dados_produtos[1]}*{preco_unidade}*{total}*{self.dados_produtos[2]}*{self.dados_produtos[3]}*{data}'
                            self.server.send(concatena.encode())
                            id_venda = self.server.recv(2048)
                            id_venda = id_venda.decode()
                            
                            id_venda = eval(id_venda)
                            id = id_venda[0][0]
                            print("Achou ID davenda")
                            
                            print(id)
                            
                            funcionario = self.tela_vendas.lineEdit_4.text()
                            cliente = self.tela_vendas.lineEdit_3.text()
                            num_casa = self.tela_vendas.lineEdit_5.text()
                            bairro = self.tela_vendas.lineEdit_6.text()
                            rua = self.tela_vendas.lineEdit_7.text()
                            
                            if(rua != '' or num_casa != '' or bairro == ''):
                                
                                concatena = f'CadastrarEntrega*{id}*{cliente}*{num_casa}*{bairro}*{rua}*{data}'
                                self.server.send(concatena.encode())
                                result = self.server.recv(2048)
                                result = result.decode()
                                print(result)
                                print("Cadastrou a entrega")

                                mensage_hist = f'Entrega para {cliente} registrada por {funcionario} no dia {data}'                        
                                concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                                self.server.send(concatena.encode())
                                result = self.server.recv(2048)
                                result = result.decode()
                                print("Adicionou Historico")

                                if(result == "True"):
                                    QMessageBox.information(None,'POOII', 'Entrega cadastrada com sucesso')
                                    self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_11)
                                    self.limpar_campos_vendas()
                                    self.dados_produtos.clear()
                            else:
                                self.tela_vendas.lineEdit_8.setText('None')
                                QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')
                                self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                                self.limpar_campos_vendas()
                                self.dados_produtos.clear()
                        else:
                            self.tela_vendas.lineEdit_8.setText('None')
                            QMessageBox.information(None,'POOII', 'Não existe essa quantidade de produto no estoque')
                            self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                            self.limpar_campos_vendas()
                            self.dados_produtos.clear()
                    except:
                        self.tela_vendas.lineEdit_8.setText('None')
                        QMessageBox.information(None,'POOII', 'A Quantidade deve ser apenas em números inteiros')
                        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)
                        self.limpar_campos_vendas()
                        self.dados_produtos.clear()
                else:
                    self.tela_vendas.lineEdit_8.setText('None')
                    QMessageBox.information(None,'POOII', 'Erro ao bsucar produto.\nID inexistente')
                    self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                    self.limpar_campos_vendas()
                    self.dados_produtos.clear()
            else:
                self.tela_vendas.lineEdit_8.setText('None')
                QMessageBox.information(None,'POOII', 'Funcionario não encontrado')
                self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                self.dados_produtos.clear()
        else:
            self.tela_vendas.lineEdit_8.setText('None')
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')
            self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
            self.limpar_campos_vendas()
            self.dados_produtos.clear()



    def BotaoRealizarVenda(self):
        """
            Realiza uma venda, verificando a disponibilidade do produto no estoque e a existência do funcionário.

            Obtém os dados da venda a partir dos campos da interface gráfica.
            Verifica a existência do funcionário no sistema.
            Verifica a existência do produto no estoque.
            Caso tudo esteja correto, adiciona a venda e registra no histórico.

        """
        
        self.dados_produtos.append(self.tela_vendas.lineEdit.text()) #CÓDIGO
        self.dados_produtos.append(self.tela_vendas.lineEdit_2.text()) #QUANTIDADE
        self.dados_produtos.append(self.tela_vendas.lineEdit_3.text()) #CLIENTE
        self.dados_produtos.append(self.tela_vendas.lineEdit_4.text()) #FUNCIONARIO
        
        if not(self.dados_produtos[0] == '' and self.dados_produtos[1] == '' and self.dados_produtos[2] == '' and self.dados_produtos[3] == ''):
            
            concatena = f'DadosUsuario*Funcionario*{self.dados_produtos[3]}'
            self.server.send(concatena.encode())
            verificacao_1 = self.server.recv(2048)
            verificacao_1 = verificacao_1.decode()
            
            concatena = f'DadosUsuario*Administrador*{self.dados_produtos[3]}'
            self.server.send(concatena.encode())
            verificacao_2 = self.server.recv(2048)
            verificacao_2 = verificacao_2.decode()
            
            verificacao_1 = eval(verificacao_1)
            verificacao_2 = eval(verificacao_2)
            
            print(verificacao_1)
            print(verificacao_2)
            
            if(len(verificacao_1) > 0 or len(verificacao_2) > 0):
                concatena = f'busca*{self.dados_produtos[0]}*Estoque*id'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()

                if(result == 'False'):
                    concatena = f'buscar_todos_dados*estoque*id*{self.dados_produtos[0]}'
                    self.server.send(concatena.encode())
                    result = self.server.recv(2048)
                    result = result.decode()

                    result = result.replace('Decimal','').replace('datetime.date','')
                    result = eval(result)
                    
                    try:
                        int(self.dados_produtos[1])
                        if(int(result[0][2]) >= int(self.dados_produtos[1])):
                            preco_unidade = result[0][5]
                            total = float(preco_unidade) * int(self.dados_produtos[1])
                            total = round(total,2)
                            data = date.today()
                            produto = result[0][1]
                            # print(self.dados_produtos)
                            
                            concatena = f'AdicionarVenda*{self.dados_produtos[0]}*{self.dados_produtos[1]}*{preco_unidade}*{total}*{self.dados_produtos[2]}*{self.dados_produtos[3]}*{data}'
                            self.server.send(concatena.encode())
                            result = self.server.recv(2048)
                            result = result.decode()

                            mensage_hist = f'Venda de um/a {produto} realizada ao cliente {self.dados_produtos[2]} pelo funcionário {self.dados_produtos[3]}'                        
                            concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                            self.server.send(concatena.encode())
                            result = self.server.recv(2048)
                            result = result.decode()

                            if(result == "True"):
                                QMessageBox.information(None,'POOII', 'Venda realizada com sucesso')
                                self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)
                                self.limpar_campos_vendas()
                                self.dados_produtos.clear()
                        else:
                            self.tela_vendas.lineEdit_8.setText('None')
                            QMessageBox.information(None,'POOII', 'Não existe essa quantidade de produto no estoque')
                            self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                            self.limpar_campos_vendas()
                            self.dados_produtos.clear()
                    except:
                        self.tela_vendas.lineEdit_8.setText('None')
                        QMessageBox.information(None,'POOII', 'A Quantidade deve ser apenas em números inteiros')
                        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)
                        self.limpar_campos_vendas()
                        self.dados_produtos.clear()
                else:
                    self.tela_vendas.lineEdit_8.setText('None')
                    QMessageBox.information(None,'POOII', 'Erro ao bsucar produto.\nID inexistente')
                    self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                    self.limpar_campos_vendas()
                    self.dados_produtos.clear()
            else:
                self.tela_vendas.lineEdit_8.setText('None')
                QMessageBox.information(None,'POOII', 'Funcionario não encontrado')
                self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
                self.dados_produtos.clear()
        else:
            self.tela_vendas.lineEdit_8.setText('None')
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')
            self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
            self.limpar_campos_vendas()
            self.dados_produtos.clear()



    def limpar_campos_vendas(self):
        """
            Remove um produto do estoque.

            Obtém o ID do produto a ser removido da interface gráfica.
            Verifica a existência do produto no estoque.
            Remove o produto do estoque e registra a remoção no histórico, se existir.

        """
        
        self.tela_vendas.lineEdit.setText('')
        self.tela_vendas.lineEdit_2.setText('')
        self.tela_vendas.lineEdit_3.setText('')
        self.tela_vendas.lineEdit_4.setText('')
        self.tela_vendas.lineEdit_8.setText('')
        



    def botaoRemoverProduto(self):
        """
            Remove um produto do estoque.

            Obtém o ID do produto a ser removido da interface gráfica.
            Verifica a existência do produto no estoque.
            Remove o produto do estoque e registra a remoção no histórico, se existir.

        """
        
        
        produto_remove = self.tela_produto.lineEdit_6.text()
        
        if not(produto_remove == ''):

            concatena = f'busca*{produto_remove}*Estoque*id'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()

            print("RESULTADO DA REMOÇÃO",result)
            
            if(result == "False"):

                concatena = f'remover_produto*{produto_remove}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()

                # self.cad.remover_produto(produto_remove)
                if (result):                    

                    data = date.today()
                    mensage_hist = f'Remoção do Produto {produto_remove} do estoque'

                    concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                    self.server.send(concatena.encode())
                    result = self.server.recv(2048)
                    result = result.decode()

                    QMessageBox.information(None,'POOII', 'Produto removido com Sucesso!')
                # self.tela_produto.lineEdit_2.setText('')
            else:
                QMessageBox.information(None,'POOII', 'Erro ao remover produto.\nID inexistente')
                # self.tela_produto.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
        self.tela_produto.lineEdit_6.setText('')



    def RemoverProdutoZeradoEstoque(self):
        """
            Este método remove produtos com quantidade zerada do estoque.
        
        """
        
        
        concatena = f'RemoverProdutoZerado'
        self.server.send(concatena.encode())
        result = self.server.recv(2048)
        result = result.decode()



    def botaoCadastrarProduto(self):
        """
            Função associada ao botão de cadastrar produto em uma interface gráfica.

            Obtém informações do produto a partir dos campos de entrada (QLineEdit) na tela de produto.
            Realiza verificações para garantir que todos os campos obrigatórios foram preenchidos.
            Calcula o preço de venda com base no preço de compra e uma margem de lucro de 45%.
            Envia uma mensagem para um servidor.
            Exibe mensagens informativas de acordo com a resposta recebida do servidor.
            Adiciona uma entrada no histórico caso o cadastro seja bem-sucedido.

    """


        produto = self.tela_produto.lineEdit_2.text()
        quantidade = self.tela_produto.lineEdit_5.text()
        preco = self.tela_produto.lineEdit_4.text()
        fornecedor = self.tela_produto.lineEdit_3.text()
        
        if not(produto == '' or preco == '' or fornecedor == '' or quantidade== ''):

            data = date.today()            
            preco_venda = (float(preco)/int(quantidade)) + ((float(preco)/int(quantidade)) * 0.45)
            
            # print("----DATA",data)
            concatena = f'cadastra_produto*{produto}*{quantidade}*{data}*{preco}*{preco_venda}*{fornecedor}'
            
            self.server.send(concatena.encode())
            resposta = self.server.recv(2048)
            resposta = resposta.decode()
            
            print(resposta)
            print("----recebeu----")

            # info_prod = Produto(produto,preco,fornecedor,data_compra)
            # if(self.cad.cadastra_produto(produto, preco, fornecedor, data_compra)):
            
            if resposta == 'True':
                
                data = date.today()
                mensage_hist = f'Cadastro do produto {produto} na quantia de {quantidade} do fornecedor {fornecedor}'
                
                concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                QMessageBox.information(None,'POOII', 'Produto cadastrado com Sucesso!')
            else:
                QMessageBox.information(None,'POOII', 'Produto ja cadastrado')
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
        self.tela_produto.lineEdit_2.setText('')
        self.tela_produto.lineEdit_3.setText('')
        self.tela_produto.lineEdit_4.setText('')
        self.tela_produto.lineEdit_5.setText('')



    def botaoCadastra(self):
        """
            Função associada ao botão de cadastro de usuário em uma interface gráfica.

            Obtém informações do usuário a partir dos campos de entrada (QLineEdit) na tela de cadastro.
            Realiza verificações de validade para o CPF e a senha.
            Verifica se o tipo de usuário foi selecionado.
            Verifica se todos os campos obrigatórios foram preenchidos.
            Verifica se o CPF já está cadastrado no sistema.
            Codifica a senha usando bcrypt antes de enviar para o servidor.
            Envia uma mensagem para o servidor (possivelmente para cadastro no sistema).
            Exibe mensagens informativas de acordo com a resposta recebida do servidor.
        """
        
        usuario = None
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
        senha = self.tela_cadastro.lineEdit_6.text()

        print(len(cpf))
        print(len(senha))
        
        usuario = self.verificar_usuario()
        
        if(len(cpf) == 11 and len(senha) >= 8):
            if usuario != None:
                if not(nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == ''):
                    
                    concatena = f'buscar_todos_dados*usuarios*cpf*{cpf}'
                    self.server.send(concatena.encode())
                    resposta = self.server.recv(2048)
                    resposta = resposta.decode()

                    resposta = eval(resposta)
                    
                    print("A resposta eh",resposta)
                    
                    if(not(resposta)):
                        # p = Pessoa(cpf,nome,endereco,nascimento,senha,usuario)
                        senha_codificada = senha.encode('utf-8')  # Codificar a senha para bytes
                        hashed = bcrypt.hashpw(senha_codificada, bcrypt.gensalt())
                        concatena = f'cadastra_ususario*{cpf}*{nome}*{endereco}*{nascimento}*{hashed}*{usuario}'
                        self.server.send(concatena.encode())
                        resposta = self.server.recv(2048)
                        resposta = resposta.decode()
                        print(resposta)
                        print("----recebeu----")

                        if (resposta):
                            
                            data = date.today()
                            mensage_hist = f'Cadastro do Usuário {nome} do tipo {usuario}'
                            
                            concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                            self.server.send(concatena.encode())
                            result = self.server.recv(2048)
                            result = result.decode()
                            
                            QMessageBox.information(None,'POOII', 'Cadastro realizado com sucesso!')
                        else:
                            QMessageBox.information(None,'POOII', 'Erro ao realizar o Cadastro')
                    else:
                        QMessageBox.information(None,'POOII', 'CPF ja cadastrado no Sistema')
                        self.limpar_campos_cad()
                else:
                    QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
                    self.limpar_campos_cad()
            else:
                QMessageBox.information(None,'POOII', 'Selecione um tipo de Usuário!')
                self.limpar_campos_cad()
            self.QtStack.setCurrentIndex(3)
            self.limpar_campos_cad()
            usuario = None
        else:
            QMessageBox.information(None,'POOII', 'CPF deve possuir 11 dígitos\nSenha deve ser maior ou igual a 8 dígitos')
            self.limpar_campos_cad()



    def limpar_campos_cad(self):
            """
                Limpa os campos de entrada na tela de cadastro.

            """
            
            self.tela_cadastro.lineEdit.setText('')
            self.tela_cadastro.lineEdit_2.setText('')
            self.tela_cadastro.lineEdit_3.setText('')
            self.tela_cadastro.lineEdit_4.setText('')
            self.tela_cadastro.lineEdit_6.setText('')



    def botaoLogin(self):
        """
            Função associada ao botão de login em uma interface gráfica.

            Obtém as informações de CPF e senha a partir dos campos de entrada (QLineEdit) na tela de login.
            Realiza verificações para garantir que ambos os campos foram preenchidos.
            Envia uma mensagem para o servidor solicitando informações sobre o usuário com o CPF fornecido.
            Realiza o processo de login, verificando a correspondência da senha com a senha armazenada no sistema.
            Redireciona para a interface correspondente com base no tipo de usuário (Administrador, Funcionário, Fornecedor, Entregador).
            Exibe mensagens informativas de acordo com o resultado do login.

        """
        
        usuario = None
        
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        
        if(cpf != '' and senha != ''):
            concatena = f'procurar_dado_especifico*usuario*usuarios*cpf*{cpf}'

            self.server.send(concatena.encode())
            usuario = self.server.recv(2048)
            usuario = usuario.decode()
            print("----recebeu----")

            print(usuario)
            self.usuario = usuario
            
            if(usuario):
                # print('Cpf login',cpf)
                # print('Senha login',senha)
                # concatena = f'procurar_dado_especifico*usuario*usuarios*cpf*{cpf}'
                # usuario = self.cad.procurar_dado_especifico('usuario','usuarios','cpf',cpf)
                # print('Usuario retornado:',usuario)
                print('usuario login',usuario)
                
                # concatena = f'buscar_usuario*{cpf}*{senha}'
                senha.encode('utf-8')
                concatena = f'Login*{cpf}*{senha}*{usuario}'

                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                
                if (result):
                    if usuario == 'Administrador':
                        self.QtStack.setCurrentIndex(3)
                        self.tela_vendas.label.setText('VENDAS')
                        self.tela_vendas.pushButton_14.setVisible(True)
                        self.tela_vendas.pushButton_2.setVisible(True)
                    elif usuario == 'Funcionario':
                        self.QtStack.setCurrentIndex(4)
                        self.tela_vendas.label.setText('VENDAS')
                        self.tela_vendas.pushButton_14.setVisible(True)
                        self.tela_vendas.pushButton_2.setVisible(True)
                    elif usuario == 'Fornecedor':
                        self.QtStack.setCurrentIndex(11)
                    elif usuario == 'Entregador':
                        self.QtStack.setCurrentIndex(10)
                        self.tela_vendas.pushButton_14.setVisible(False)
                        self.tela_vendas.pushButton_2.setVisible(False)
                        self.tela_vendas.label.setText('Entregador')
                        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_7)
                        # self.tela_entregador.PAGINAS.setCurrentWidget(self.tela_entregador.page_7)
                else:
                    QMessageBox.information(None,'POOII', 'CPF ou senha não encontrado')
                    self.tela_login.lineEdit.setText('')
                    self.tela_login.lineEdit_2.setText('')
            else:
                QMessageBox.information(None,'POOII', 'Erro na busca do Usuário')
                self.tela_login.lineEdit.setText('')
                self.tela_login.lineEdit_2.setText('')
            usuario = None
        else:
            QMessageBox.information(None,'POOII', 'Todos os campos devem estar preenchido')
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')

    def botaoExibirAdministradores(self):
        """
            Função associada ao botão para exibir informações sobre administradores em uma tabela na interface gráfica.

            Envia uma mensagem para o servidor solicitando a lista de administradores.
            Recebe a resposta do servidor, que contém a lista de administradores.
            Atualiza a tabela na interface gráfica com as informações recebidas.

        """
        
        concatena = f'ListarUsuario*Administrador'
        
        self.server.send(concatena.encode())
        lista_adm = self.server.recv(2048)
        lista_adm = lista_adm.decode()
        
        lista_adm = eval(lista_adm)

        self.tela_usuario.tableWidget.setRowCount(len(lista_adm))
        self.tela_usuario.tableWidget.setColumnCount(6)

        for i in range (0, len(lista_adm)):
            for j in range(0, 6):
                self.tela_usuario.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_adm[i][j])))



    def botaoExibirFuncionario(self):
        """
            Função associada ao botão para exibir informações sobre funcionários em uma tabela na interface gráfica.

            Envia uma mensagem para o servidor solicitando a lista de funcionários.
            Recebe a resposta do servidor, que contém a lista de funcionários.
            Atualiza a tabela na interface gráfica com as informações recebidas.

        """
        
        concatena = f'ListarUsuario*Funcionario'

        self.server.send(concatena.encode())
        lista_adm = self.server.recv(2048)
        lista_adm = lista_adm.decode()

        lista_adm = eval(lista_adm)

        self.tela_usuario.tableWidget.setRowCount(len(lista_adm))
        self.tela_usuario.tableWidget.setColumnCount(6)

        for i in range (0, len(lista_adm)):
            for j in range(0, 6):
                self.tela_usuario.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_adm[i][j])))



    def botaoExibirFornecedor(self):
        """
            Função associada ao botão para exibir informações sobre fornecedores em uma tabela na interface gráfica.

            Envia uma mensagem para o servidor solicitando a lista de fornecedores.
            Recebe a resposta do servidor, que contém a lista de fornecedores.
            Atualiza a tabela na interface gráfica com as informações recebidas.

        """
        
        
        concatena = f'ListarUsuario*Fornecedor'

        self.server.send(concatena.encode())
        lista_adm = self.server.recv(2048)
        lista_adm = lista_adm.decode()

        lista_adm = eval(lista_adm)

        self.tela_usuario.tableWidget.setRowCount(len(lista_adm))
        self.tela_usuario.tableWidget.setColumnCount(6)

        for i in range (0, len(lista_adm)):
            for j in range(0, 6):
                self.tela_usuario.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_adm[i][j])))



    def botaoExibirEntregador(self):
        """
            Função associada ao botão para exibir informações sobre entregadores em uma tabela na interface gráfica.

            Envia uma mensagem para o servidor solicitando a lista de entregadores.
            Recebe a resposta do servidor, que contém a lista de entregadores.
            Atualiza a tabela na interface gráfica com as informações recebidas.

        """
        
        concatena = f'ListarUsuario*Entregador'

        self.server.send(concatena.encode())
        lista_adm = self.server.recv(2048)
        lista_adm = lista_adm.decode()

        lista_adm = eval(lista_adm)

        self.tela_usuario.tableWidget.setRowCount(len(lista_adm))
        self.tela_usuario.tableWidget.setColumnCount(6)

        for i in range (0, len(lista_adm)):
            for j in range(0, 6):
                self.tela_usuario.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_adm[i][j])))



    def botaoRemoverUsuario(self):
        """
            Função associada ao botão para remover um usuário do sistema.

            Obtém as informações de tipo de usuário e nome do usuário a partir dos campos de entrada (QLineEdit) na tela de usuário.
            Realiza verificações para garantir que ambos os campos foram preenchidos.
            Envia mensagens para o servidor para buscar e verificar a existência do usuário com base no tipo e no nome fornecidos.
            Se o usuário for encontrado, envia uma mensagem para o servidor solicitando a remoção do usuário.
            Atualiza o histórico com a informação da remoção e exibe mensagens informativas de acordo com o resultado.

        """


        tipo_usuario = self.tela_usuario.lineEdit_6.text()
        nome_usuario = self.tela_usuario.lineEdit_7.text()
        
        if not(tipo_usuario == '' and nome_usuario == ''):
            
            concatena = f'busca*{tipo_usuario}*usuarios*usuario'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            print("Verificar usuario:", result)
            
            if(result == 'False'):
                
                concatena = f'busca*{nome_usuario}*usuarios*nome'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                print("Verificar nome:", result)
                
                if(result == 'False'):
                    
                    concatena = f'RemoverUsuario*{tipo_usuario}*{nome_usuario}'
                    self.server.send(concatena.encode())
                    result = self.server.recv(2048)
                    result = result.decode()
                    print("Verificar remoção:", result)
                    
                    if(result == 'True'):
                        
                        data = date.today()
                        mensage_hist = f'Remoção do Usuário {nome_usuario} do tipo {tipo_usuario}'
                        
                        concatena = f'AdicionarHistorico*{mensage_hist}*{data}'
                        self.server.send(concatena.encode())
                        result = self.server.recv(2048)
                        result = result.decode()
                        
                        mensage = f'Remoção do usuário realizada com sucesso!'
                        QMessageBox.information(None,'POOII',mensage)
                        self.tela_usuario.lineEdit_7.setText('')
                        self.tela_usuario.lineEdit_6.setText('') 
                    else:
                        mensage = f'Algo deu errado!'
                        QMessageBox.information(None,'POOII',mensage)
                        self.tela_usuario.lineEdit_7.setText('')
                        self.tela_usuario.lineEdit_6.setText('') 
                else:
                    mensage = f'nome {nome_usuario} não encontrado'
                    QMessageBox.information(None,'POOII',mensage)
                    self.tela_usuario.lineEdit_7.setText('')
                    self.tela_usuario.lineEdit_6.setText('') 
            else:
                mensage = f'Usuário {tipo_usuario} não encontrado'
                QMessageBox.information(None,'POOII',mensage)
                self.tela_usuario.lineEdit_7.setText('')
                self.tela_usuario.lineEdit_6.setText('') 
        else:
            QMessageBox.information(None,'POOII','Todos os campos devem estar preenchido')



    def botaoBuscarUsuario(self):
        """
            Função associada ao botão para buscar informações de um usuário no sistema.

            Obtém as informações de tipo de usuário e nome do usuário a partir dos campos de entrada (QLineEdit) na tela de usuário.
            Realiza verificações para garantir que ambos os campos foram preenchidos.
            Envia mensagens para o servidor para buscar e verificar a existência do usuário com base no tipo e no nome fornecidos.
            Se o usuário for encontrado, envia uma mensagem para o servidor solicitando os dados do usuário.
            Atualiza uma tabela na interface gráfica com as informações recebidas e exibe mensagens informativas de acordo com o resultado.

        """
        
        tipo_usuario = self.tela_usuario.lineEdit_8.text()
        nome_usuario = self.tela_usuario.lineEdit_9.text()
        
        if not(tipo_usuario == '' and nome_usuario == ''):
            
            concatena = f'busca*{tipo_usuario}*usuarios*usuario'
            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            print("Verificar usuario:", result)
            
            if(result == 'False'):
                
                concatena = f'busca*{nome_usuario}*usuarios*nome'
                self.server.send(concatena.encode())
                result = self.server.recv(2048)
                result = result.decode()
                print("Verificar id:", result)
                
                if(result ==  'False'):
                    
                    concatena = f'DadosUsuario*{tipo_usuario}*{nome_usuario}'
                    self.server.send(concatena.encode())
                    lista_adm = self.server.recv(2048)
                    lista_adm = lista_adm.decode()
                    
                    lista_adm = eval(lista_adm)
                    print(lista_adm)
                    
                    self.tela_usuario.tableWidget_2.setRowCount(len(lista_adm))
                    self.tela_usuario.tableWidget_2.setColumnCount(6)

                    for i in range (0, len(lista_adm)):
                        for j in range(0, 6):
                            self.tela_usuario.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_adm[i][j])))
                            
                    self.tela_usuario.lineEdit_8.setText('')
                    self.tela_usuario.lineEdit_9.setText('')
                else:
                    mensage = f'Nome {nome_usuario} não encontrado'
                    QMessageBox.information(None,'POOII',mensage)
                    self.tela_usuario.lineEdit_8.setText('')
                    self.tela_usuario.lineEdit_9.setText('')
            else:
                mensage = f'Usuário {tipo_usuario} não encontrado'
                QMessageBox.information(None,'POOII',mensage)
                self.tela_usuario.lineEdit_8.setText('')
                self.tela_usuario.lineEdit_9.setText('') 
        else:
            QMessageBox.information(None,'POOII','Todos os campos devem estar preenchido')



    def BuscarProduto(self):
        """
            Função associada à busca de informações sobre um produto no sistema.

            Obtém o ID do produto a ser buscado a partir do campo de entrada (QLineEdit) na tela de produto.
            Realiza verificações para garantir que o campo foi preenchido.
            Envia uma mensagem para o servidor para buscar todos os dados do produto com base no ID fornecido.
            Atualiza uma tabela na interface gráfica com as informações recebidas e exibe mensagens informativas de acordo com o resultado.

        """

        produto_busca = self.tela_produto.lineEdit.text()
        if not(produto_busca == ''):

            concatena = f'buscar_todos_dados*Estoque*id*{produto_busca}'
            self.server.send(concatena.encode())
            lista_produtos = self.server.recv(2048)
            lista_produtos = lista_produtos.decode()

            lista_produtos = lista_produtos.replace('Decimal','').replace('datetime.date','')
            lista_produtos = eval(lista_produtos)
            
            if(lista_produtos):
                print("----resultado----",lista_produtos)
                
                # lista_produtos = eval(lista_produtos)

                self.tela_produto.tableWidget_2.setRowCount(1)
                self.tela_produto.tableWidget_2.setColumnCount(7)

                for i in range(0,7):
                    self.tela_produto.tableWidget_2.setItem(0,i,QtWidgets.QTableWidgetItem(str(lista_produtos[0][i])))
                    self.tela_produto.lineEdit.setText('')
            else:
                QMessageBox.information(None,'POOII', 'Valor não encontrado!')
                self.tela_produto.lineEdit.setText('')

        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')



    def BuscarProdutoFuncionario(self):
        """
            Função associada à busca de informações sobre um produto no sistema, destinada a funcionários.

            Obtém o ID do produto a ser buscado a partir do campo de entrada (QLineEdit) na tela de estoque destinada a funcionários.
            Realiza verificações para garantir que o campo foi preenchido.
            Envia uma mensagem para o servidor para buscar todos os dados do produto com base no ID fornecido.
            Atualiza uma tabela na interface gráfica com as informações recebidas e exibe mensagens informativas de acordo com o resultado.

        """
        
        produto_busca = self.tela_estoque_funcionario.lineEdit.text()
        if not(produto_busca == ''):

            concatena = f'buscar_todos_dados*Estoque*id*{produto_busca}'
            self.server.send(concatena.encode())
            lista_produtos = self.server.recv(2048)
            lista_produtos = lista_produtos.decode()

            lista_produtos = lista_produtos.replace('Decimal','').replace('datetime.date','')
            lista_produtos = eval(lista_produtos)
            
            if(lista_produtos):
                print("----resultado----",lista_produtos)
                
                # lista_produtos = eval(lista_produtos)

                self.tela_estoque_funcionario.tableWidget_2.setRowCount(1)
                self.tela_estoque_funcionario.tableWidget_2.setColumnCount(7)

                for i in range(0,7):
                    if(i != 4):
                        self.tela_estoque_funcionario.tableWidget_2.setItem(0,i,QtWidgets.QTableWidgetItem(str(lista_produtos[0][i])))
                    else:
                        self.tela_estoque_funcionario.tableWidget_2.setItem(0,i,QtWidgets.QTableWidgetItem('--'))
                    self.tela_estoque_funcionario.lineEdit.setText('')
            else:
                QMessageBox.information(None,'POOII', 'Valor não encontrado!')
                self.tela_estoque_funcionario.lineEdit.setText('')

        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')



    def ListarProdutos(self):
        """
            Função associada à listagem de todos os produtos disponíveis no sistema.

            Envia uma mensagem para o servidor solicitando a lista de todos os produtos.
            Recebe a lista de produtos do servidor e a converte de string para uma estrutura de dados (lista de listas).
            Atualiza uma tabela na interface gráfica com as informações recebidas.

        """
        
        concatena = f'ListarProdutos'
        self.server.send(concatena.encode())
        lista_produtos = self.server.recv(2048)
        lista_produtos = lista_produtos.decode()
        
        lista_produtos = lista_produtos.replace('Decimal','').replace('datetime.date','')
        lista_produtos = eval(lista_produtos)

        self.tela_produto.tableWidget_3.setRowCount(len(lista_produtos))
        self.tela_produto.tableWidget_3.setColumnCount(7)

        for i in range (0, len(lista_produtos)):
            for j in range(0, 7):
                self.tela_produto.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_produtos[i][j])))



    def ListarProdutosFuncionario(self):
        """
            Função associada à listagem de todos os produtos disponíveis no sistema, destinada a funcionários.

            Envia uma mensagem para o servidor solicitando a lista de todos os produtos.
            Recebe a lista de produtos do servidor e a converte de string para uma estrutura de dados (lista de listas).
            Atualiza uma tabela na interface gráfica (tela de estoque destinada a funcionários) com as informações recebidas.

        """
        
        concatena = f'ListarProdutos'
        self.server.send(concatena.encode())
        lista_produtos = self.server.recv(2048)
        lista_produtos = lista_produtos.decode()
        
        lista_produtos = lista_produtos.replace('Decimal','').replace('datetime.date','')
        lista_produtos = eval(lista_produtos)

        self.tela_estoque_funcionario.tableWidget_3.setRowCount(len(lista_produtos))
        self.tela_estoque_funcionario.tableWidget_3.setColumnCount(7)

        for i in range (0, len(lista_produtos)):
            for j in range(0, 7):
                if(j != 4):
                    self.tela_estoque_funcionario.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_produtos[i][j])))
                else:
                    self.tela_estoque_funcionario.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem('--'))


    def voltarTelaInicial(self):
        """
            Função associada ao retorno à tela inicial do sistema.

            Define o índice da pilha de widgets (QtStack) para a posição 0, que representa a tela inicial.
            Limpa os campos de entrada na tela de login.

        """
        
        self.QtStack.setCurrentIndex(0)
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')



    def sair(self):
        """
            Função associada ao encerramento da aplicação.

            Utiliza a função sys.exit() para encerrar a execução da aplicação.

        """
        
        sys.exit()




    def onClicked(self, checkBox):
        """
            Manipulador de eventos associado ao clique em uma caixa de seleção.

            Verifica se a caixa de seleção está marcada. Se estiver marcada, atualiza a opção selecionada
            com o texto da caixa de seleção.

            Parameters:
            ----------
            checkBox (QtWidgets.QCheckBox): A caixa de seleção que foi clicada.

        """
        
        if checkBox.isChecked():
            self.opcao_selecionada = checkBox.text()



    def verificar_usuario(self):
        """
            Verifica qual tipo de usuário foi selecionado na tela de cadastro.

            Retorna o tipo de usuário selecionado. Atualiza o estado das caixas de seleção após a verificação.

            Returns:
            ----------
            usuario : str
        
        """
        
        usuario = None
        # self.tela_cadastro.checkBox.toggled.connect(lambda: self.onClicked(self.checkBox))
        # self.tela_cadastro.checkBox_2.toggled.connect(lambda: self.onClicked(self.checkBox2))
        # self.tela_cadastro.checkBox_3.toggled.connect(lambda: self.onClicked(self.checkBox3))
        # self.tela_cadastro.checkBox_4.toggled.connect(lambda: self.onClicked(self.checkBox4))
        
        if self.tela_cadastro.checkBox.isChecked():
            usuario = self.tela_cadastro.checkBox.text()
            self.tela_cadastro.checkBox.setChecked(False)
        if self.tela_cadastro.checkBox_2.isChecked():
            usuario = self.tela_cadastro.checkBox_2.text()
            self.tela_cadastro.checkBox_2.setChecked(False)
        if self.tela_cadastro.checkBox_3.isChecked():
            usuario = self.tela_cadastro.checkBox_3.text()
            self.tela_cadastro.checkBox_3.setChecked(False)
        if self.tela_cadastro.checkBox_4.isChecked():
            usuario = self.tela_cadastro.checkBox_4.text()
            self.tela_cadastro.checkBox_4.setChecked(False)

        print(usuario)

        return usuario



    def botaoExibirHistorico(self):
        """
            Solicita e exibe o histórico de atividades do sistema.

            Envia uma solicitação ao servidor para obter o histórico de atividades, 
            recebe os dados, formata e exibe na tabela correspondente.

        """
        
        concatena = f'ExibirHistorico'
        self.server.send(concatena.encode())
        dados_hist = self.server.recv(2048)
        dados_hist = dados_hist.decode()
        
        dados_hist = dados_hist.replace('datetime.date','')
        dados_hist = eval(dados_hist)

        self.tela_historico.tableWidget.setRowCount(len(dados_hist))
        self.tela_historico.tableWidget.setColumnCount(3)

        for i in range (0, len(dados_hist)):
            for j in range(0,3):
                self.tela_historico.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_hist[i][j])))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
