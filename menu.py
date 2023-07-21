from colorama import init, Fore, Style
from input import ControllerInputHandler
from configs import ConfigHandler
import os
import about

configHandler = ConfigHandler()
controllerInputHandler = ControllerInputHandler()


class DisplayMenu:
    init()

    def clear_console(self):
        os.system("cls")

    def display_menu(self):
        print(Fore.MAGENTA + "===== WI-FI Car Control Pannel =====")
        print(Fore.BLUE + "1. Configurations")
        print(Fore.GREEN + "2. Controller")
        print(Fore.CYAN + "3. About")
        print(Fore.RED + "4. Exit")
        print(Fore.MAGENTA + "====================================")
        print(Style.RESET_ALL)

    def get_user_choice(self):
        while True:
            user_choice = controllerInputHandler.get_char_input()
            if ord(user_choice) >= 49 and ord(user_choice) <= 52:
                choice = int(user_choice)
                return choice

    def configurations(self):
        self.clear_console()
        configHandler.config_menu()
        self.clear_console()

    def controller(self):
        # print("You selected Controller")
        self.clear_console()
        controllerInputHandler.get_controller_input()
        self.clear_console()

    def about(self):
        self.clear_console()
        about.show_about()
        self.clear_console()

    def menu(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.configurations()
            elif choice == 2:
                self.controller()
            elif choice == 3:
                self.about()
            elif choice == 4:
                print("Exiting the menu.")
                break
