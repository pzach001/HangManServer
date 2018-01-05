
HangmanServer was coded for UCR CS164 Networks Final Project

Setup: 
NOTE: Hangmans server works by using the mininet emulator as its network and then using telnet as its clients
1. Download and setup mininet:  
    - Here is a website on how to download and setup using VirtualBox :
2. After mininet is setup create a network emulation through 
        http://www.brianlinkletter.com/set-up-mininet/
3. This program was written with Python

How to run HangmanServer:
1. After running mininet and setting up a network emulation, ssh into network using command:
        ssh -X -p [Port] mininet@[HOSTIPADDRESS] 
        (ex:  ssh -X -p 2222 mininet@localhost)
        to set port look at this : https://www.quora.com/How-can-I-ssh-into-my-VM-from-the-Mac-OS-X-host


2. running the server:
    - To run the server use command: "python server.py" in where server file is located
    - This should setup the server in which you can type admin user input or wait for clients to give you input

3. running the client:
    - To run a client , I used Telnet:
    - Running this will create a client process and connect it with the server:  
                    "Telnet [HostIP] [serverdefinedPort]"
            - HostIp is your localhost ip address
            - ServerdefindPort is the port number you can initialize in the server code, it is currently initalized to 1114
            ex) telnet 127.0.0.1 1114
    - to make multiple clients repeat the steps in the "running the client" section per client . 
-Now your server and clients should be ready to play the hangman game!
   


