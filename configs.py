import msvcrt
from colorama import init, Fore, Style
import os

init()

# This is file where our Ip and Port address are located
CONFIG_FILE = "nodemcu_config.txt"


class ConfigHandler:
    # This fxn helps to get single character input at a time like getch() in C
    def get_char_input(self):
        while True:
            char = msvcrt.getch()
            if char in (
                b"\r",
                b"\n",
            ):  # Check for Enter key (carriage return or line feed)
                continue
            return char.decode("utf-8")

    # This fxn is used to read config data from the config file
    def read_config(self):
        try:
            with open(CONFIG_FILE, "r") as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    nodeMCU_ip = lines[0].strip()
                    nodeMCU_port = int(lines[1])
                    return nodeMCU_ip, nodeMCU_port

        except FileNotFoundError:
            return "0.0.0.0", "0000"

    # def update_config(nodeMCU_ip, nodeMCU_port):
    #     with open(CONFIG_FILE, "w") as file:
    #         file.write(nodeMCU_ip + "\n")
    #         file.write(nodeMCU_port)
    #         print("Configs Updated")

    # Nativate to the fxn according to users choice
    def get_user_choice(self):
        while True:
            user_choice = self.get_char_input()
            return user_choice

    # Fxn for viewing the config file in console
    def config_menu_view(self):
        node_mcu_ip, node_mcu_port = self.read_config()
        print(Fore.RED + "=======VIEW CONFIG=====================")
        print(Fore.WHITE + f"IP Address: {node_mcu_ip}")
        print(Fore.WHITE + f"Port Address: {node_mcu_port}")
        print(Fore.RED + "========================================")

    # Fxn for updating the config file in console
    def config_menu_update(self):
        print(Fore.RED + "=======UPDATE CONFIG=====================")
        node_mcu_ip = input(Fore.WHITE + "IP Address: ")
        node_mcu_port = input(Fore.WHITE + "PORT Address: ")
        with open(CONFIG_FILE, "w") as file:
            file.write(node_mcu_ip + "\n")
            file.write(node_mcu_port)
            print("Configs Updated")
        print(Fore.RED + "========================================")

    # Displays the Config menu for user
    def config_menu(self):
        while True:
            print(Fore.RED + "=======CONFIGURATION MENU===============")
            print(Fore.GREEN + "1. View Configs")
            print(Fore.YELLOW + "2. Edit Configs")
            print(Fore.RED + "========================================")
            choice = self.get_user_choice()
            if choice == "1":
                os.system("cls")
                self.config_menu_view()
            elif choice == "2":
                os.system("cls")
                self.config_menu_update()
            elif choice == "q":
                break
