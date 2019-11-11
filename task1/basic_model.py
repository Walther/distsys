import socket
import threading


def provide_service():
    """ provide data to clients """
    pass


def start_server(ip_port, client_num):
    """ a server to deal with queries from other nodes """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ip_port)
    server.listen(client_num)
    print("start listening")

    while True:
        client, addr = server.accept()
        new_client = threading.Thread(target=provide_service, args=(client, addr))
        new_client.start()
    
    server.close()


def start_client(ip_port):
    """ a client to retrieve temperature from other nodes """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip_port)

    client.close()


def main():
    local_server = threading.Thread(start_server, args=(ip_port, client_num))
    local_server.start()

    while True:
        """ when need to check to temperature, start a client """
        start_client(ip_port)
