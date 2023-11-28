import sys
import mysql.connector as mysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from Telas.tela_inicial import *
from Telas.tela_cadastro import *
from Telas.tela_produto import *
from Telas.tela_login import *
from Telas.tela_bem_vindo import * #ADMINISTRADOR
from Telas.tela_entregador import * #ENTREGADOR
from Telas.tela_funcionario import * #FUNCIONARIO
from Telas.tela_fornecedores import * #FONECEDOR

from server_cliente import *
# from server_servidor import *

from pessoa import Pessoa
from cadastro import Cadastro
from login import Login
from produto import Produto

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

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.server = server_cliente('10.180.42.112',4050)
        self.log = Login()
        self.cad = Cadastro()
        # self.prod = Produto()
        self.opcao_selecionada = None
        
        self.tela_bem_vindo.pushButton_8.clicked.connect(self.abrirTelaCadastro) #botao cadastrar tela administrador
        self.tela_bem_vindo.pushButton_7.clicked.connect(self.abrirTelaProduto)
        
        # funções dos botões da tela principal
        self.tela_inicial.pushButton_3.clicked.connect(self.sair) # funções dos botões da tela principal
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)
        # self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.abrirTelaBemVindo)

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
        self.tela_produto.pushButton_8.clicked.connect(self.botaoRemoverProduto)

    def botaoRemoverProduto(self):
        produto_remove = self.tela_produto.lineEdit_6.text()
        
        if not(produto_remove == ''):
            if not (self.cad.busca(produto_remove,'produtos','id')):
                self.cad.remover_produto(produto_remove)
                QMessageBox.information(None,'POOII', 'Produto removido com Sucesso!')
                # self.tela_produto.lineEdit_2.setText('')
            else:
                QMessageBox.information(None,'POOII', 'Erro ao remover produto.\nID inexistente')
                # self.tela_produto.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
        self.tela_produto.lineEdit_6.setText('')

    def botaoCadastrarProduto(self):
        produto = self.tela_produto.lineEdit_2.text()
        preco = self.tela_produto.lineEdit_5.text()
        fornecedor = self.tela_produto.lineEdit_4.text()
        data_compra = self.tela_produto.lineEdit_3.text()
        
        if not(produto == '' or preco == '' or fornecedor == '' or data_compra== ''):
            info_prod = Produto(produto,preco,fornecedor,data_compra)
            
            if(self.cad.cadastra_produto(info_prod)):
                QMessageBox.information(None,'POOII', 'Produto cadastrado com Sucesso!')
            else:
                QMessageBox.information(None,'POOII', 'Erro ao realizar o Cadastro do produto')
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
            print(usuario)
            print(nome)
            print(cpf)
            print(endereco)
            print(senha)
            print(nascimento)
            if not(nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == ''):
                # p = Pessoa(cpf,nome,endereco,nascimento,senha,usuario)
                concatena = f'cadastra_ususario*{cpf}*{nome}*{endereco}*{nascimento}*{senha}*{usuario}'
                self.server.send(concatena.encode())
                resposta = self.server.recv(2048)
                resposta = resposta.decode()
                print(resposta)
                print("----recebeu----")

                if (resposta):
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
            if (self.cad.buscar_usuario(cpf,senha)):
                if usuario == 'Administrador':
                    self.QtStack.setCurrentIndex(3)
                elif usuario == 'Funcionario':
                    self.QtStack.setCurrentIndex(4)
                elif usuario == 'Fornecedor':
                    self.QtStack.setCurrentIndex(5)
                elif usuario == 'Entregador':
                    self.QtStack.setCurrentIndex(6)
            else:
                QMessageBox.information(None,'POOII', 'Erro na busca do Usuário')
                self.tela_login.lineEdit.setText('')
                self.tela_login.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,'POOII', 'CPF ou senha não encontrado')
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
        usuario = None


    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
        
    def abrirTelaProduto(self):
        self.QtStack.setCurrentIndex(7)

    def abrirTelaLogin(self): 
        self.QtStack.setCurrentIndex(2)

    def TelaProdutoFrameAdicionar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page)
        
    def TelaProdutoFrameListar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_2)
        
    def TelaProdutoFrameBuscar(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_3)
        
    def TelaProdutoFrameRemover(self):
        self.tela_produto.PAGINAS.setCurrentWidget(self.tela_produto.page_4)
    
    def ListarProdutos(self):
        lista_produtos = self.cad.ListarProdutos()
        
        concatena = f'ListarProdutos'
        self.server.send(concatena.encode())
        lista_produtos = self.server.recv(2048)
        lista_produtos = lista_produtos.decode()
        print("----recebeu----")
        
        self.tela_produto.tableWidget_3.setRowCount(len(lista_produtos))
        self.tela_produto.tableWidget_3.setColumnCount(4)

        for i in range (0, len(lista_produtos)):
            for j in range(0, 4):
                self.tela_produto.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(lista_produtos[i][j])))
        
    def voltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')

    def abrirTelaBemVindo(self):
        self.QtStack.setCurrentIndex(3)

    def sair(self):
        sys.exit()

    def onClicked(self, radioButton):
        if radioButton.isChecked():
            self.opcao_selecionada = radioButton.text()

    def verificar_usuario(self):
        usuario = None
        self.tela_cadastro.radioButton.toggled.connect(lambda: self.onClicked(self.radioButton))
        self.tela_cadastro.radioButton_2.toggled.connect(lambda: self.onClicked(self.radioButton2))
        self.tela_cadastro.radioButton_3.toggled.connect(lambda: self.onClicked(self.radioButton3))
        self.tela_cadastro.radioButton_4.toggled.connect(lambda: self.onClicked(self.radioButton4))

        if self.tela_cadastro.radioButton.isChecked():
            usuario = self.tela_cadastro.radioButton.text()
        if self.tela_cadastro.radioButton_2.isChecked():
            usuario = self.tela_cadastro.radioButton_2.text()
        if self.tela_cadastro.radioButton_3.isChecked():
            usuario = self.tela_cadastro.radioButton_3.text()
        if self.tela_cadastro.radioButton_4.isChecked():
            usuario = self.tela_cadastro.radioButton_4.text()

        print(usuario)
        return usuario

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
