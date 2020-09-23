# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 13:24'

import dns.resolver

domain = input('Please input an domain: ')
ns = dns.resolver.resolve(domain, 'NS')   # 指定查询类型为NS记录
for i in ns.response.answer:
    # print(i)
    # print(i.items)
    for j in i.items:
        # print(j)
        print(j.to_text())
