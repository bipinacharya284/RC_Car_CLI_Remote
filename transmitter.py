import socket
from configs import ConfigHandler


def setup_config():
    configHandler = ConfigHandler()
    ip, port = configHandler.read_config()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock


def send_message(sock, message):
    sock.sendall(message.encode())
    ack = sock.recv(1024)
    print("Ack Received: ", ack.decode())
