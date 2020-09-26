# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/6 16:01'

# 读取人物名称
f = open('name.txt')
data = f.read()
print(data)
# print(data.split('|'))

# 读取兵器名称
f2 = open('weapon.txt', 'r', encoding='UTF-8')  # 'r'可以省略
# data2 = f2.read()
# print(data2)

i = 1
for line in f2.readlines():
    if i % 2 == 1:
        # print(line.strip('\n'))
        print(line.strip())
    i += 1
#
# f3 = open('sanguo.txt', encoding='UTF-8')
# data3 = f3.read()
# print(data3.replace('\n', ''))


# def func(filename):
#     print(open(filename).read())
#     print('test func')
#
#
# func('name.txt')

