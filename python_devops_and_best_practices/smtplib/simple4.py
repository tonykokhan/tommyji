# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 14:37'

import smtplib
from email.mime.multipart import MIMEMultipart  # 导入MIMEMultipart类
from email.mime.text import MIMEText		# 导入MIMEText类
from email.mime.image import MIMEImage		# 导入MIMEImage类

HOST = 'smtp.163.com'			# 定义smtp主机
SUBJECT = u"官网业务服务质量周报"  # 定义邮件主题
TO = "781712767@qq.com"			# 定义邮件接收人
FROM = "tonykokhan@163.com"		# 定义邮件发件人


def addimg(src, imgid):				# 添加图片函数，参数1：图片路径，参数2：图片id
    fp = open(src, 'rb')			# 打开文件
    msgImage = MIMEImage(fp.read())		# 创建MIMEImage对象，读取图片内容作为参数
    fp.close()					# 关闭文件
    msgImage.add_header('Content-ID', imgid)  # 指定图片文件的Content-ID,<img> 标签src用到
    return msgImage				# 返回msgImage对象


msg = MIMEMultipart('related')			# 创建MIMEMultipart对象，采用related定义内嵌资源的邮件体

# 创建一个MIMEText对象，HTML元素包括文字与图片<img>
msgtext = MIMEText(
    "<font color=red> 官网业务周平均延时图表：<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>",
    "html",
    "utf-8")
msg.attach(msgtext)				# MIMEMultipart对象附加MIMEText的内容
# 使用MIMEMultipart对象附加MIMEImage的内容
msg.attach(addimg("img/weekly.png", "weekly"))

# 创建一个MIMEText对象，附加week_report.xlsx文档
attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"  # 指定文件格式类型

# 指定Content-Disposition值为attachment则出现下载保存对话框，保存的默认文件名使用filename指定
# 由于qqmail使用gb18030页面编码，为保证中文文件名不出现乱码，对文件名进行编码转换
attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报（12周）.xlsx\"". decode(
    "utf-8").encode("gb18030")

msg.attach(attach)		# MIMEMultipart对象附加MIMEText附件内容
msg['Subject'] = SUBJECT  # 邮件主题
msg['From'] = FROM		# 邮件发件人，邮件头部可见
msg['To'] = TO			# 邮件收件人，邮件头部可见
try:
    server = smtplib.SMTP()  # 创建一个SMTP()对象
    server.connect(HOST, "25")  # 通过connect方法连接smtp主机
    server.starttls()		# 启动安全传输模式
    server.login("tonykokhan@163.com", "tommyji813")  # 邮箱账号登录校验
    server.sendmail(FROM, TO, msg.as_string())		# 邮件发送
    server.quit()		# 断开smtp连接
    print("邮件发送成功！")
except Exception as e:
    print("失败：" + str(e))
