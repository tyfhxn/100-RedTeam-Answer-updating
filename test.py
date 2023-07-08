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


eth_ip = get_ethernet_ip()
print(eth_ip)
