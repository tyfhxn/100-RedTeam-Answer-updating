import socket
import os
import sys

i = 1
# 1初始化套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_socket.setblocking(False)
# 设置地址可以复用，解决了 端口没有及时释放的问题
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# https://blog.csdn.net/qulang4358/article/details/91633093
# 第三个参数：　　0　　（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议
'''
https://blog.csdn.net/linuxerhqt/article/details/6526902
第一个参数表示套接字描述符，使用SOL_SOCKET表示可以自己设置选项，这里的选项为第二个参数的几个取值
第二个参数有如下几种选择：
SO_DEBUG:打开或关闭调试信息
SO_REUSEADDR: 打开或关闭地址复用功能
SO_DONTROUTE：打开或关闭路由查找功能
SO_BROADCAST: 允许或禁止发送广播数据
SO_SNDBUF：设置发送缓冲区大小
           发送缓冲区的大小是有上下限的，其上限为256 * (sizeof(struct sk_buff) + 256)，
           下限为2048字节。该操作将sock->sk->sk_sndbuf设置为val * 2，之所以要乘以2，是防
           止大数据量的发送，突然导致缓冲区溢出。最后，该操作完成后，因为对发送缓冲的大小 作了改变，要检查sleep队列，如果有进程正在等待写，将它们唤醒。
SO_RCVBUF:设置接受缓冲区大小
'''
# 2 获取IP，服务器绑定ip和port
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
tcp_socket.bind((ip, 11000))

# 3 设置为被动监听模式  最大并发接收的数量是128
tcp_socket.listen(128)
# recv_buff = tcp_socket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
# send_buff = tcp_socket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
# print('接受区缓冲大小：{}'.format(recv_buff))
# print('发送缓冲区大小：{}'.format(send_buff))
# tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
# print('接受区缓冲大小：{}'.format(recv_buff))
while True:
    # 4 等待接收链接请求  接收到一个元组 （客户端的socket对象，(客户端的地址,端口)）
    client, addr = tcp_socket.accept()
    # print('client:', client)
    # print('addr:', addr)
    while True:
        try:
            data = client.recv(4096)
            print(data.decode('gbk'))
            if not data:
                # 如果数据为空 说明客户端关闭了链接  这里的client也就可以关闭
                client.close()
                break
            text = '---------'
            client.send(text.encode('gbk'))
        except:
            print("客户端链接中断")
            sys.exit()
            #
            # i += 1
            # if i != 1:
            #     break
# 5断开
tcp_socket.close()



# TCP编程的服务器端一般步骤是：

# 创建一个socket，用函数socket()；
# 设置socket属性，用函数setsockopt(); * 可选
# 绑定IP地址、端口等信息到socket上，用函数bind();
# 开启监听，用函数listen()；
# 接收客户端上来的连接，用函数accept()；
# 收发数据，用函数send()和recv()，或者read()和write();
# 关闭网络连接；
# 关闭监听；