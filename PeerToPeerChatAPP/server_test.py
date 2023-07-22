import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on port {port}")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024)
        if data:
            print(f"Received from client: {data.decode()}")
            message = "."
            conn.sendall(message.encode())
            if message == "Q":
                conn.close()
                break


if __name__ == "__main__":
    start_server()
