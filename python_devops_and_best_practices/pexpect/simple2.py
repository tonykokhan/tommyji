# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 16:13'

# expect方法有两个非常棒的成员：before与after。before成员保存了最近匹配成功之前的内容，after成员保存了最近匹配成功之后的内容
import pexpect
import sys

child = pexpect.spawn('ssh root@10.0.0.220')
fout = open('mylog.txt', 'w')
child.logfile = fout

child.expect(["password:"])
child.sendline("Ableyf@2016")
print("before:" + child.before)
print("after:" + child.after)
