#!/bin/python3

#Sockets

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#af_inet is the IPV4 address
#sock_stream is basically a port

s.connect((HOST, PORT))
