import socket 

def server_cliente(ip, port):
    """
        Essa função ela cria uma comunicação entre o cliente e o servidor.

        O endereço ip indentifica a máquina na rede e a porta especifica o serviço em execução nessa máquina.

        Parameters:
        ----------
        ip : char 
            Usado para atribuir identificadores exclusivos a cada dispositivo em uma rede.
        port : int
            Usado para designar a porta específica a qual um serviço ou processo está associado em um rede.

        Returns:
        ----------
        client_socket : socket
        Quando o servidor aceita uma conexão com um cliente, ele cria um novo objeto de soquete para interagir com esse cliente.
    """
    ip = ip
    port = port
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket
