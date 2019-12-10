# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 17:32'


def counter(FIRST=0):
    cnt = [FIRST]   # 定义一个列表，指定一个元素，初始值设为0

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num5 = counter(5)
num10 = counter(10)


# # print(counter()())
# num1 = counter()
# print(num1)
# print(num1())
# print(num1())
# print(num1())
# print(num1())
# print(num1())
# print(num1())

print(num5())
print(num5())
print(num5())
print(num10())
print(num10())
print(num10())
