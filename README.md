# RC_Car_CLI_Remote
This project is made to control Wifi based RC car. Only CLI interface is developed till now.

<h3>Dependencies required for contributing to my project:<h3>
    &nbsp;-> pip install pyinstaller // For making standalone .exe file<br>
        &nbsp;&nbsp;-> pyinstaller --onefile scriptFile.py<br>
    &nbsp;-> pip install colorama // For colored text<br>
    &nbsp;-> pip install msvcrt // For taking single char input<br>


<h3>Instruction For Using Application</h3>
    &nbsp;-> .exe file is found inside dist/ folder<br>
    &nbsp;-> Enter (menu number) to navigate to menu<br>
    &nbsp;-> Press q key to quit from sub-menu<br>
    &nbsp;-> From menu you can configure Ip and port to use controller<br>
    &nbsp;-> Controller uses WSAD for operation and q to quit.<br> 
    &nbsp;-> ** If IP address and Port not setup then program crashes<br>
    &nbsp;-> For writing ip and port address it comes from nodeMCU in the case of controlling car and for testing the server_test.exe have configured it.<br>
    &nbsp;-> testing server have port as 12345.<br>
    &nbsp;-> For ip we need to go to cmd and type ipconfig, it give ipv4 address and you need to enter that address for server_test only.<br>
    
