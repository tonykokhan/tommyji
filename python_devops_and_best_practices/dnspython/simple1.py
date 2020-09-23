# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 11:09'

import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
A = dns.resolver.resolve(domain, 'A')		# 指定查询类型为A记录
for i in A.response.answer:			# 通过response.answer方法获取查询回应信息
    for j in i.items:				# 遍历回应信息
        if j.rdtype == 1:
            print(j.address)
