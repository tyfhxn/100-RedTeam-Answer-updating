socket完成网络通信必备

打开链接--->传输数据--->关闭连接



if \_\_name\__='__main\_\_'  解释

> 当哪个模块被直接执行时，该模块“__name__”的值就是“__main__”，当被导入另一模块时，“__name__”的值就是模块的真实名称。用一个类比来解释一下：记得小时候要轮流打算教室，轮到自己的时候（模块被直接执行的时候），我们会说今天是“我”（__main__）值日，称呼其他人时，我们就会直接喊他们的名字。所以，“__main__”就相当于当事人，或者说第一人称的“我”。
>
> 所以，当运行“if \__name__=='\_\_main_\_':”语句时，如果当前模块时被直接执行，__name__的值就是__main__，条件判断的结果为True，“if __name__=='__main__':”下面的代码块就会被执行。



创建套接字：

```python
import socket
#创建套接字
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #第一个参数是协议族，第二个参数是通信类型，如TCP,UDP
socket.AF_INET  IPV4
socket.SOCK_STREAM   TCP流
·······功能
s.close()
```

