import socket

host = "192.168.0.140"
port = 5980
addr = (host, port)
tcpCussocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCussocket.connect(addr)
text = input("输入")
tcpCussocket.send(text.encode('gbk'))
