# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 15:17'

# 实现远程SSH登录，登录成功后显示/home目录文件清单，并通过日志文件记录所有的输入与输出
import pexpect
import sys

child = pexpect.spawn('ssh root@10.0.0.220')    # windows下不支持spawn，参考：https://www.cnblogs.com/xiaofanguoguo/p/4976072.html
# fout = file('mylog.txt', 'w')   # python3废弃了file()
fout = open('mylog.txt', 'w')
child.logfile = fout
# child.logfile = sys.stdout    # 系统标准输出

child.expect("password:")
child.sendline("Ableyf@2016")
child.expect('#')
child.sendline('ls /home')
child.expect('#')
