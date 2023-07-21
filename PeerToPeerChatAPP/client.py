import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter host ip")
    port = 12345

    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Connection to the server failed.")
        return

    while True:
        message = input("Enter a message to send: ")
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode()}")

    print("connection closed")
    client_socket.close()


if __name__ == "__main__":
    start_client()
