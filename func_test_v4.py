# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 17:05'


def func():
    a = 1
    b = 2
    return a+b


def sum(a):         # 外部函数
    def add(b):     # 内部函数
        return a+b  # 外部函数的变量被内部函数引用的情况就叫做闭包（内部函数引用外部变量的写法就叫闭包）
    return add      # 返回的是内部函数的函数名称

# add 函数名称或函数的引用
# add() 函数的调用


num1 = func()
num2 = sum(2)   # num2相当于sum()外部函数里面的内部函数
print(num2(4))
# print(type(num1))
# print(type(num2))


