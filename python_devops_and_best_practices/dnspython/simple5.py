# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 13:40'

import dns.resolver
import os
import http.client

iplist = []			# 定义域名IP列表变量
# appdomain = "www.google.com.hk"  # 定义业务域名
appdomain = "appstudent.zhihuishu.com"
# appdomain = "www.2144.cn"


def get_iplist(appdomain=""):  # 域名解析函数，解析成功IP将被追加到iplist
    try:
        r = dns.resolver.resolve(appdomain, 'A')  # 解析A记录类型
        # r = dns.resolver.resolve("www.zhihuishu.com", "A")  # 解析A记录类型
        # for i in r.response.answer:
        #     print(i.items)
        #     for j in i.items:
        #         print(j)
    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in r.response.answer:
        # print(i.items)
        for j in i.items:
            # print(j)
            if j.rdtype == 1:   # A记录
                # print(j.rdtype)
                iplist.append(j.address)  # 追加到iplist
                return iplist
            # elif j.rdtype == 5:     # CNMAE记录
            #     print(j.rdtype)
            #     iplist.append(j)  # 追加到iplist
            #     print(iplist)
        # return True     # 为什么加了这行就不返回A记录了？个人理解：因为加了这条相当于不返回任何数据


def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    http.client.socket.setdefaulttimeout(5)		# 定义http连接超时时间（5秒）
    conn = http.client.HTTPConnection(checkurl)  # 创建http连接对象

    try:
        conn.request("GET", "/", headers={"Host": appdomain})  # 发起URL请求，添加host主机头
        r = conn.getresponse()
        getcontent = r.read(7)			# 获取URL页面前7个字符，以便做可用性校验
    finally:
        if getcontent == "success":  # 监控URL页的内容一般是事先定义好的，比如“HTTP200”等
            print(ip + " [OK]")
        else:
            print(ip + " [Error]")			# 此处可放告警程序，可以是邮件、短信通知


if __name__ == "__main__":
    # if get_iplist(appdomain) and len(iplist) > 0:  # 条件：域名解析正确且至少返回一个IP
    #     for ip in iplist:
    #         checkip(ip)
    # else:
    #     print("dns resolver error.")

    if get_iplist(appdomain):
        # print(iplist)
        for ip in iplist:
            print(ip)
            checkip(ip)
    else:
        print("sai")
