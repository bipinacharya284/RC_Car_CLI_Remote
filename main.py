from menu import DisplayMenu
from configs import ConfigHandler
import transmitter

configHandler = ConfigHandler()


def main():
    ip, port = configHandler.read_config()
    # print(ip, port)
    displayMenu = DisplayMenu()
    if ip == "0.0.0.0" or port == "0000":
        sock = ""
    else:
        try:
            sock = transmitter.setup_config(ip, port)
        except ConnectionRefusedError:
            print("Machine Offline")
            displayMenu.menu("")
        displayMenu.menu(sock)


if __name__ == "__main__":
    main()
