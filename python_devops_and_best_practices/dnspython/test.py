# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 15:51'

import dns.resolver

r = dns.resolver.resolve("www.zhihuishu.com", "A")

for i in r.response.answer:
    print(i.items)
