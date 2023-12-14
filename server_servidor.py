import socket
from backend.cadastro import *
import threading
# from database.senha import senha

class ClienteThread(threading.Thread):
    """
        Instancia um Thread para que a execução simultânea do banco
        aplicações seja possível.

        Attributes
        ---------
        clientSock : socket.socket
            Soquete de conexão para enviar e receber solicitações.
        clientAddress : str
            Endereço IP de conexão

        Methods
        -------
        run(self)
            inicializar a thread
    """

    def __init__(self, clientSock, clientAddress):
        """
            Construtor da classe ClienteThread.

            Parameters
            ----------
            clientSock: socket.socket
                Soquete de conexão para enviar e receber solicitações.
            clientAddress : str
                Endereço IP de conexão.
        """
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
        """
            Inicia a execução da thread.

            A thread espera por solicitações do cliente e as processa de acordo com o método fornecido. 
            O método é chamado dinamicamente, usando reflexão. 
            O cliente é desconectado quando o método 'sair' é chamado. 
        """
        try:
            while True:
                solicit = self.clientSock.recv(2048).decode().split("*")
                print("-------FUNÇÂO-------",solicit)
                # Buscando o método da requisição no banco
                if solicit:
                    metodo = solicit.pop(0)
                    if metodo == 'sair':
                        self.clientSock.close()
                        break
                    banco = Cadastro()
                    func = getattr(banco, metodo)
                    # executando o método e passando todos os parametros que foram recebidos na requisição
                    retorno = func(*solicit)
                    self.clientSock.send(f'{retorno}'.encode('utf-8'))
        except AttributeError:
            print('Algo deu errado')

class Servidor():
    """
        A Classe servidor espera por conexões e quando elas são feitas,
        os envia para a threads.

        Attributes
        ----------
        host : str
            localhost para fazer conexões.
        port : str
            Porta de acesso para fazer conexões
        server : socket.socket
            Soquete de conexão para enviar e receber solicitações.

        Methods
        -------
        start(self)
            Executa o servidor para que ele aguarde as conexões.

    """
    def __init__(self, host):
        """
            Construtor da classe Servidor.

            Parameters
            ----------
            host : str
                localhost para fazer conexões.
        """
        self.host = host 
        self.port = 4050
        addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicia o socket
        self.serv_socket.bind(addr) #define as portas e quais ips podem se conectar com o servidor
        self.serv_socket.listen(10) #define o limite de conexões

        
    def start(self):
        """
            Aguarda a conexão de um cliente, cria uma nova thread para lidar com suas solicitações e inicia essa thread.
        """
        while True:
            print("aguardando conexão...\n\n")
            client_sock, client_address = self.serv_socket.accept() 
            print(f'Cliente {client_address[0]} conectado.\n\n')
            print("aguardando solicitação...\n\n")

            novaThread = ClienteThread(client_sock, client_address)

            print("Thread inciada\n\n")
            novaThread.start()

    
if __name__ == '__main__':
    print(f'Ip do servidor: 10.180.44.101\n\n')
    c = Servidor('10.180.44.101')
    c.start()