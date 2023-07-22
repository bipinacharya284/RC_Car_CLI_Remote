import socket


# setups the connection environment
def setup_config(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock


# sends message
def send_message(sock, message):
    sock.sendall(message.encode())
    ack = sock.recv(1024)
    print("Ack Received: ", ack.decode())
