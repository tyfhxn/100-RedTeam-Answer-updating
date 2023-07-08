import socket
import random

import wmi

# 1初始化套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 2建立链接  要传入链接的服务器ip和port
def get_ethernet_ip():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        # print(interface.IPAddress[0] + '----' + interface.Description)
        if 'Realtek PCIe GbE Family Controller' in interface.Description:
            # print(interface)
            ip = interface.IPAddress[0]
            return ip
    return None


ip = get_ethernet_ip()
tcp_socket.connect((ip, 5980))

while True:
    text = input('发送的数据')
    # 判断输入是否为空：防止出现input接受空值导致进程死锁
    while text == "":
        text = input("不允许为空")
    # 3发数据
    tcp_socket.send(text.encode('gbk'))
    # 4接收数据
    data = tcp_socket.recv(1024)
    print(data.decode('gbk'))

# 5断开
# tcp_socket.close()

# TCP编程的客户端一般步骤是：

# 创建一个socket，用函数socket()；
# 设置socket属性，用函数setsockopt();* 可选
# 绑定IP地址、端口等信息到socket上，用函数bind();* 可选
# 设置要连接的对方的IP地址和端口等属性；
# 连接服务器，用函数connect()；
# 收发数据，用函数send()和recv()，或者read()和write();
# 关闭网络连接；
