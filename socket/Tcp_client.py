#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = "54.169.17.69"
port = 12345                # Reserve a port for your service.
print host,port
s.connect((host, port))

s.sendall('Here I am!')

print s.recv(1024)
s.close                     # Close the socket when done