from colorama import init, Fore, Style
import transmitter
import msvcrt


init()


class ControllerInputHandler:
    # To get one character input at once.
    def get_char_input(self):
        while True:
            char = msvcrt.getch()
            if char in (
                b"\r",
                b"\n",
            ):  # Check for Enter key (carriage return or line feed)
                continue
            return char.decode("utf-8")

    # to get users controller input
    def get_controller_input(self):
        sock = transmitter.setup_config()
        print(Fore.BLUE + "Keyboard Controller Activated (q to quit):")
        while True:
            user_input = self.get_char_input()

            if user_input.lower() == "w":
                transmitter.send_message(sock, "F")
                print(Fore.GREEN + "Forward")

            if user_input.lower() == "s":
                transmitter.send_message(sock, "B")
                print(Fore.RED + "Backward")

            if user_input.lower() == "a":
                transmitter.send_message(sock, "L")
                print(Fore.MAGENTA + "Left")

            if user_input.lower() == "d":
                transmitter.send_message(sock, "R")
                print(Fore.YELLOW + "Right")

            if user_input.lower() == "q":
                break
