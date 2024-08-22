# Python-TCP-IP-Socket-Connection

This script sets up a network connection from your computer to a server running on the same machine (localhost) at port 7777, using a TCP/IP connection. I used NetCat to listen and confirm the connection.
</br>
1. Imports the Socket Library:
 </br>
 - `import socket` imports the necessary Python library to create network connections.
</br>
2. Defines the Server Details:
   </br> 
 - `HOST = '127.0.0.1'` sets the IP address to connect to (localhost, which is your own computer).
 - </br>
 - `PORT = 7777` sets the port number to connect to on the server.
 - </br>

3. Creates a Socket:
 </br>
 - `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)` creates a socket object for communication.
 - </br>
 - `AF_INET` specifies using an IPv4 address.
 - </br>
 - `SOCK_STREAM` indicates the use of TCP (Transmission Control Protocol).
 - </br>

4. Connects to the Server:
 </br>
 - `s.connect((HOST, PORT))` establishes a connection to the server at the specified IP address and port.
