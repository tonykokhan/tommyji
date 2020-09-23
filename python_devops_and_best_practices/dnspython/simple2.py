# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/23 11:09'

import dns.resolver

domain = input('Please input an domain: ')
MX = dns.resolver.resolve(domain, 'MX')   # 指定查询类型为MX记录
for i in MX:                            # 遍历回应结果，输出MX记录的preference及exchange信息
    print('MX preference =', i.preference, 'mail exchanger =', i.exchange)
