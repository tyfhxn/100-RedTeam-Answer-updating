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
while True:
    send_date = input("请输入数据：")
    if send_date == 'exit':
        break
    ip = get_ethernet_ip()
    udp_socket.sendto(send_date.encode('gbk'), (ip, 9999))

udp_socket.close()
