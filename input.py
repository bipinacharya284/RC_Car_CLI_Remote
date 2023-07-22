from colorama import init, Fore, Style
import transmitter
import msvcrt
from configs import ConfigHandler
import socket

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
    def get_controller_input(self, sock):
        print(Fore.BLUE + "Keyboard Controller Activated (q to quit):")
        while True:
            user_input = self.get_char_input()

            if user_input.lower() == "w":
                print(Fore.GREEN + "Forward")
                transmitter.send_message(sock, "F")

            if user_input.lower() == "s":
                print(Fore.RED + "Backward")
                transmitter.send_message(sock, "B")

            if user_input.lower() == "a":
                print(Fore.MAGENTA + "Left")
                transmitter.send_message(sock, "L")

            if user_input.lower() == "d":
                print(Fore.YELLOW + "Right")
                transmitter.send_message(sock, "R")

            if user_input.lower() == "q":
                transmitter.send_message(sock, "Q")
                break
