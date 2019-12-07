# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/7 14:39'

# print('abc', end='\n\n')
# print('abc', end='\n')
# print('abc')


# def func(a, b, c):
#     print('a = %s' % a)
#     print('b = %s' % b)
#     print('c = %s' % c)
#
#
# # func(1, 2, 3)
# # func(1, c=3, b=2)   # 使用关键字参数可以忽略顺序
# func(1, c=3)


# # 取得参数的个数
# def howlong(first, *other):
#     # return len(first) + len(other)
#     # return 1 + len(other)
#     print(len(first) + len(other))
#     # print(1 + len(other))
#
#
# howlong('123', 456, 789, 1, 2, 3)
# # howlong(123)
# # howlong()


var1 = 123


def func():
    print(var1)


func()