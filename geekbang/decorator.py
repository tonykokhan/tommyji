# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 20:10'

import time
# print(time.time())
# time.sleep(3)
# print(time.time())


def timer(func):    # 闭包和装饰器的区别：闭包传递进来的是变量，内部的函数引用的也是变量；装饰器传递进来的是函数，内部的函数引用的也是一个函数
    def wrapper():
        start_time = time.time()
        func()  # 注意是一个函数
        stop_time = time.time()
        print("运行时间是 %s 秒" % (stop_time-start_time))
    return wrapper


@timer
def i_can_sleep():
    # time.sleep(3)           # 直接调用也相当于return（直接调用不需要return）
    print(time.sleep(3))        # 如果直接打印函数（注意这里是函数），相当于函数没有设置返回值，故返回None
    # return time.sleep(3)      # return之后的语句不会执行

# print(timer(i_can_sleep()))
# start_time = time.time()
i_can_sleep()
# 执行过成类似下面两行：
# num = timer(i_can_sleep())
# num()
# print(num)
# print(type(num))
# stop_time = time.time()
# print('函数运行了 %s 秒' % (stop_time-start_time))









