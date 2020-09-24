# -*- coding: utf-8 -*-
from __future__ import unicode_literals		# 使用unicode编码
__author__ = 'tommyji'
__date__ = '2020/9/24 17:27'

# 实现一个自动化FTP操作
import pexpect
import sys

child = pexpect.spawn('ftp 47.110.151.143')
child.expect('(?i)name .*: ')
child.sendline('arexam')

child.expect('(?i)password')
child.sendline('arexam')

child.expect('ftp> ')
child.sendline('bin')

child.expect('ftp> ')
child.sendline('get rebots.txt')

child.expect('ftp> ')
sys.stdout.write(child.before)

print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
child.sendline('bye')
child.close()
