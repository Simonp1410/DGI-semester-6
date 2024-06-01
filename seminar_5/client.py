import socket

client = socket.socket()

client.connect(('localhost', int(3000)))

client.close()