# UDP编程的服务器端一般步骤是：

# 创建一个socket，用函数socket()；
# 设置socket属性，用函数setsockopt();* 可选
# 绑定IP地址、端口等信息到socket上，用函数bind();
# 循环接收数据，用函数recvfrom();
# 关闭网络连接；
# UDP编程的客户端一般步骤是：
import socket

import wmi


def get_ethernet_ip():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        # print(interface.IPAddress[0] + '----' + interface.Description)
        if 'Realtek PCIe GbE Family Controller' in interface.Description:
            # print(interface)
            ip = interface.IPAddress[0]
            return ip
    return None


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = get_ethernet_ip()
udp_socket.bind((ip, 9999))
while True:
    receive_date = udp_socket.recvfrom(1024)
    if receive_date == 'exit1':
        break
    print(receive_date)

udp_socket.close()
