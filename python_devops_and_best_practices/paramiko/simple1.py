# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/25 10:12'

import paramiko

hostname = '120.26.44.175'
port = '28793'
username = 'root'
password = ''
paramiko.util.log_to_file('syslogin.log')  # 发送paramiko日志到syslogin.log文件

ssh = paramiko.SSHClient()			# 创建一个ssh客户端client对象
ssh.load_system_host_keys()			# 获取客户端host_keys，默认~/.ssh/known_hosts，非默认路径需指定
ssh.connect(
    hostname=hostname,
    port=int(port),
    username=username,
    password=password)  # 创建ssh连接
stdin, stdout, stderr = ssh.exec_command('ls')  # 调用远程执行命令方法exec_command()
print(stdout.read())		# 打印命令执行结果，得到Python列表形式，可以使用stdout.readlines()
ssh.close()					# 关闭ssh连接
