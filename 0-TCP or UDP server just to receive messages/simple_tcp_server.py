import socket
import time

host = "192.168.0.140"
port = 5980
bufsiz = 1024
addr = (host, port)
# AF_UNIX用于同一台机器上的进程间通信，AF_INET对于IPV4协议的TCP和UDP
tcpSerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSocket.bind(addr)
while True:
    tcpSerSocket.listen(1)
    client, c_port = tcpSerSocket.accept()
    print(client, end="\n")
    print(c_port, end="\n")
    data = client.recv(bufsiz)
    print(data.decode('gbk'))
    exit()
