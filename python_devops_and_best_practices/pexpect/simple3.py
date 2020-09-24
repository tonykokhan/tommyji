# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 16:25'

# 使用pxssh类实现一个ssh连接远程主机并执行命令
from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()  # 创建pxssh对象s
    hostname = input('hostname: ')
    port = input('port: ')
    username = input('username: ')
    password = getpass.getpass('please input password: ')  # 接收密码输入
    s.login(hostname, username, password, port=port)  # 建立ssh连接，注意port=port
    s.sendline('uptime')  # 运行uptime命令
    s.prompt()			# 匹配系统提示符
    print(s.before)		# 打印出现系统提示符前的命令输出。到此才会打印uptime命令的输出
    s.sendline('ls -l')
    s.prompt()
    print(s.before)
    s.sendline('df')
    s.prompt()
    print(s.before)
    s.logout()  # 断开ssh连接
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(str(e))
