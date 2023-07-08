import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_date = input("请输入数据：")
    if send_date == 'exit':
        break
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    udp_socket.sendto(send_date.encode('gbk'), (ip, 9999))

udp_socket.close()
