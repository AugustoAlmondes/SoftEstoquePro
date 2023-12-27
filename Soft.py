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
    def setupUi(self, Main):
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
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.server = server_cliente('192.168.18.107',4050)
        self.dados_produtos = []
        
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

    def abrirTelaBemVindo(self):
        self.QtStack.setCurrentIndex(3)
        self.RemoverProdutoZeradoEstoque()

    def AbrirTelaFuncionario(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaProduto(self):
        self.QtStack.setCurrentIndex(7)

    def abrirTelaUsuario(self):
        self.QtStack.setCurrentIndex(8)

    def abrirTelaLogin(self): 
        self.QtStack.setCurrentIndex(2)

    def abrirTelaHistorico(self):
        self.QtStack.setCurrentIndex(9)

    def abrirTelaVendas(self):
        self.QtStack.setCurrentIndex(10)

    def TelaProdutoFrameAdicionar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page)
        
    def TelaProdutoFrameListar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_2)
        
    def TelaProdutoFrameBuscar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_3)
        
    def TelaProdutoFrameRemover(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_4)

    def TelaUsuarioListar(self):
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_2)
        
    def TelaUsuarioRemover(self):
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_4)
        
    def TelaUsuarioBuscar(self):
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page_3)
        
    def TelaUsuarioTipos(self):
        self.tela_usuario.PAGINAS.setCurrentWidget(self.tela_usuario.page)    

    def AbrirTelaVendaEntrega(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_3)

    def TelaVendasFrameInicial(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_11)

    def TelaVendasFrameRealizarVenda(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page)
    
    def TelaVendasFrameTotal(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_2)
    
    def AbrirFrameEntrega(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_7)
    
    def AbrirFrameBuscarEntrega(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_10)
    
    def AbrirFrameFinalizarEntrega(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_9)
    
    def AbrirFrameListarEntrega(self):
        self.tela_vendas.PAGINAS.setCurrentWidget(self.tela_vendas.page_8)

    def TelaProdutoFrameListarFuncionario(self):
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_2)

    def TelaProdutoFrameBuscarFuncionario(self):
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_3)

    def AbrirTelaEstoqueFuncionario(self):
        self.QtStack.setCurrentIndex(11)
        self.tela_estoque_funcionario.PAGINAS.setCurrentWidget(self.tela_estoque_funcionario.page_5)

    def botaoFinalizarEntrega(self):
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
                    mensage_hist = f'Entrega de id {codigo} finalizada'
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
        self.tela_vendas.lineEdit.setText('')
        self.tela_vendas.lineEdit_2.setText('')
        self.tela_vendas.lineEdit_3.setText('')
        self.tela_vendas.lineEdit_4.setText('')
        self.tela_vendas.lineEdit_8.setText('')
        



    def botaoRemoverProduto(self):
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
        concatena = f'RemoverProdutoZerado'
        self.server.send(concatena.encode())
        result = self.server.recv(2048)
        result = result.decode()



    def botaoCadastrarProduto(self):
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
        usuario = None
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
        senha = self.tela_cadastro.lineEdit_6.text()

        usuario = self.verificar_usuario()

        if usuario != None:
            if not(nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == ''):
                # p = Pessoa(cpf,nome,endereco,nascimento,senha,usuario)
                concatena = f'cadastra_ususario*{cpf}*{nome}*{endereco}*{nascimento}*{senha}*{usuario}'
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
                QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
                self.limpar_campos_cad()
        else:
            QMessageBox.information(None,'POOII', 'Selecione um tipo de Usuário!')
            self.limpar_campos_cad()
        self.QtStack.setCurrentIndex(3)
        self.limpar_campos_cad()
        usuario = None



    def limpar_campos_cad(self):
            self.tela_cadastro.lineEdit.setText('')
            self.tela_cadastro.lineEdit_2.setText('')
            self.tela_cadastro.lineEdit_3.setText('')
            self.tela_cadastro.lineEdit_4.setText('')
            self.tela_cadastro.lineEdit_6.setText('')



    def botaoLogin(self):
        usuario = None
        
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        concatena = f'procurar_dado_especifico*usuario*usuarios*cpf*{cpf}'

        self.server.send(concatena.encode())
        usuario = self.server.recv(2048)
        usuario = usuario.decode()
        print("----recebeu----")

        print(usuario)
        
        if(usuario):
            # print('Cpf login',cpf)
            # print('Senha login',senha)
            # concatena = f'procurar_dado_especifico*usuario*usuarios*cpf*{cpf}'
            # usuario = self.cad.procurar_dado_especifico('usuario','usuarios','cpf',cpf)
            # print('Usuario retornado:',usuario)
            print('usuario login',usuario)
            
            concatena = f'buscar_usuario*{cpf}*{senha}'

            self.server.send(concatena.encode())
            result = self.server.recv(2048)
            result = result.decode()
            
            if (result):
                if usuario == 'Administrador':
                    self.QtStack.setCurrentIndex(3)
                elif usuario == 'Funcionario':
                    self.QtStack.setCurrentIndex(4)
                elif usuario == 'Fornecedor':
                    self.QtStack.setCurrentIndex(5)
                elif usuario == 'Entregador':
                    self.QtStack.setCurrentIndex(6)
            else:
                QMessageBox.information(None,'POOII', 'CPF ou senha não encontrado')
                self.tela_login.lineEdit.setText('')
                self.tela_login.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII', 'Erro na busca do Usuário')
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
        usuario = None



    def botaoExibirAdministradores(self):
        
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
        self.QtStack.setCurrentIndex(0)
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')



    def sair(self):
        sys.exit()



    def onClicked(self, checkBox):
        if checkBox.isChecked():
            self.opcao_selecionada = checkBox.text()



    def verificar_usuario(self):
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
