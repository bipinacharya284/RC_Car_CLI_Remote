from colorama import init, Fore, Style
from input import ControllerInputHandler

controllerInputHandler = ControllerInputHandler()


init()


def show_about():
    while True:
        exitMainLoop = False
        print(Fore.RED + "=======ABOUT APPLICATION DEVELOPER======")
        print(
            Fore.BLUE
            + "This application is developed for the purpose of conrolling RC car using wifi module"
        )
        print(Fore.CYAN + "Github:github.com/bipinacharya284")
        print(Fore.YELLOW + "Dont Forgot to Give a STAR")
        print(Fore.RED + "========================================")
        while True:
            user_input = controllerInputHandler.get_char_input()
            if user_input == "q":
                exitMainLoop = True
                break
        if exitMainLoop == True:
            break
