# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 15:51'

import dns.resolver

# iplist = []			# 定义域名IP列表变量
appdomain = "www.baidu.com"


def get_iplist(domain=""):  # 域名解析函数，解析成功IP将被追加到iplist
    iplist = []
    try:
        A = dns.resolver.resolve(domain, 'A')  # 解析A记录类型
    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            # print(j)
            if j.rdtype == 1:   # A记录
                iplist.append(j.address)  # 追加到iplist
                if len(iplist) > 0:
                    print(iplist)
    print("----------------------------------")
    if len(iplist) > 0:
        print(iplist)


if __name__ == "__main__":
    get_iplist(appdomain)
