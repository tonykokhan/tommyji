# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/7 16:16'

with open('redis.txt') as f:
    # data = f.read()         # 读取整个文件，将文件内容放到一个字符串变量中
    # data = f.readline()     # 每次读取一行；返回的是一个字符串对象，保村当前行到内存
    # data = f.readlines()    # 一次性读取整个文件；自动将文件内容分析成一个行的列表。读取所有行然后把它们作为一个字符串列表返回
    for line in f:
        data = f.read().replace('\n', ', ')

print(data)
