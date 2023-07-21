# RC_Car_CLI_Remote
This project is made to control Wifi based RC car. Only CLI interface is developed till now.

Dependencies required for contributing to my project:
    -> pip install pyinstaller // For making standalone .exe file
        -> pyinstaller --onefile scriptFile.py
    -> pip install colorama // For colored text
    -> pip install msvcrt // For taking single char input


Instruction For Using Application
    -> .exe file is found inside dist/ folder
    -> Enter (menu number) to navigate to menu
    -> Press q key to quit from sub-menu
    -> From menu you can configure Ip and port to use controller
    -> Controller uses WSAD for operation and q to quit. 
    -> ** If IP address and Port not setup then program crashes
    -> For writing ip and port address it comes from nodeMCU in the case of controlling car and for testing the server_test.exe have configured it.
    -> testing server have port as 12345.
    -> For ip we need to go to cmd and type ipconfig, it give ipv4 address and you need to enter that address for server_test only.
    -> 
