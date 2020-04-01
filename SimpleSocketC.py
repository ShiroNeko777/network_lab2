import socket

TCP_IP = 'localhost'
TCP_PORT = 7272
BUFFER_SIZE = 1024
MESSAGE = "你好!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(MESSAGE).encode())
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data.decode())
