# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 20:29'


# 带参数的wrapper
def tips(func):
    def wrapper(a, b):
        print('start')
        func(a, b)
        print('stop')
    return wrapper


@tips
def sai(a, b):
    print(a+b)
    # return (a+b)


@tips
def sub(a, b):
    print(a-b)


# add(4, 5)
print(sai(4, 5))    # None由此返回
# sai(4, 5)
# print(sub(7, 3))
