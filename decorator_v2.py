# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 20:29'


def tips(func):
    def wrapper(a, b):
        print('start')
        func(a, b)
        print('stop')
    return wrapper


@tips
def add(a, b):
    print(a+b)


@tips
def sub(a, b):
    print(a-b)


print(add(4, 5))
print(sub(7, 3))
