# -*- coding: utf-8 -*-
import pexpect
import sys

# 远程文件自动打包并下载
ip = "10.0.0.220"					# 定义目标主机
user = "root"					# 目标主机用户
passwd = "Ableyf@2016"				# 目标主机密码
target_file = "/data/logs/nginx_access.log"  # 目标主机nginx日志文件

child = pexpect.spawn('/usr/bin/ssh', [user + '@' + ip])  # 运行ssh命令
fout = open('mylog.txt', 'w')				# 输入、输出日志写入mylog.txt文件
child.logfile = fout

try:
    child.expect('(?i)password')  # 匹配password字符串，(?i)表示不区别大小写
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czPf /data/nginx_access.tar.gz ' + target_file)  # 打包nginx日志文件
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except EOFError:
    print("expect EOF")
except TimeoutError:
    print("expect TIMEOUT")

child = pexpect.spawn('/usr/bin/scp', [user + '@' + ip + ':/data/nginx_access.tar.gz', '/home'])  # 启动scp远程拷贝命令，实现将打包好的nginx日志复制至本地/home目录
fout = open('mylog.txt', 'a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)  # 匹配缓冲区EOF（结尾），保证文件复制正常完成
except EOFError:
    print("expect EOF")
except TimeoutError:
    print("expect TIMEOUT")
