# -*- coding: utf-8 -*-
from __future__ import unicode_literals		# 使用unicode编码
__author__ = 'tommyji'
__date__ = '2020/9/24 17:27'

# 实现一个自动化FTP操作
import pexpect
import sys

child = pexpect.spawn('ftp ftp.openbsd.org')  # 运行ftp命令
child.expect('(?i)name .*: ')			# (?i)表示后面的字符串正则匹配忽略大小写
child.sendline('anonymous')			# 输入ftp账号信息

child.expect('(?i)password')			# 匹配密码输入提示
child.sendline('pexpect@soureceforge.net')  # 输入ftp密码

child.expect('ftp> ')
child.sendline('bin')				# 启用二进制传输模式

child.expect('ftp> ')
child.sendline('get rebots.txt')		# 下载robots.txt文件

child.expect('ftp> ')
sys.stdout.write(child.before)			# 输出匹配“ftp> ”之前的输入与输出

print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
# 调用interact()让出控制权，用户可以继续当前的会话手工控制子程序，默认输入“^]”字符跳出child.interact()
child.sendline('bye')
child.close()
