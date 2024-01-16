import socket 

def server_cliente(ip, port):
    """
        Cria e conecta a um socket de cliente para se comunicar com o servidor.

        Parameters
        ----------
        ip : str
            O endereço IP do servidor.
        port : int
            O número da porta do servidor.

        Returns
        -------
        socket : socket
        Um objeto de soquete conectado ao servidor.
    """
    
    ip = ip
    port = port
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket
