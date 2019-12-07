# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/7 16:16'

with open('redis.txt') as f:
    # data = f.readlines()
    for line in f:
        data = f.read().replace('\n', ', ')

print(data)
