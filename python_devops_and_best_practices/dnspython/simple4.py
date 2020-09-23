# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 13:37'

import dns.resolver

# r = dns.resolver.resolve("www.zhihuishu.com", "A")    # 写A记录会返回两条结果
r = dns.resolver.resolve("www.zhihuishu.com", "CNAME")

# domain = input('Please input an domain: ')
# cname = dns.resolver.resolve(domain, 'CNAME')     # 指定查询类型为CNAME记录
#
# for i in cname.response.answer:                 # 结果将回应cname后的目标域名
#     print(i)
#     for j in i.items:
#         print(j.to_text())
#         print(type(j))
#         if j.rdtype == 5:
#             print(j.rdtype)

# print("qname:", r.qname)
# print("rdtype:", r.rdtype)
for i in r.response.answer:
    # print(i)
    print(i.items)
    for j in i.items:
        print("address:", j)
