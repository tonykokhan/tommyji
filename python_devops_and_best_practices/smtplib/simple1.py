# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 12:24'

import smtplib
import string

HOST = "smtp.163.com"			# 定义smtp主机
SUBJECT = "Test email from Python"  # 定义邮件主题
TO = "781712767@qq.com"			# 定义邮件收件人
FROM = "tonykokhan@163.com"		# 定义邮件发件人
text = "Python rules them all!"		# 邮件内容
BODY = "\r\n".join([			# 组装sendmail方法的邮件主题内容，各段以"\r\n"进行分隔
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text]
),
server = smtplib.SMTP()				# 创建一个SMTP()对象
server.connect(HOST, "25")			# 通过connect方法连接smtp主机
# server.starttls()				# 启动安全传输模式
server.login("tonykokhan@163.com", "tommyji813")  # 邮箱账号登录校验
server.sendmail(FROM, [TO], BODY)		# 邮件发送
server.quit()					# 断开smtp连接
