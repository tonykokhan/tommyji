# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/10 20:10'

import time
# print(time.time())
# time.sleep(3)
# print(time.time())


def timer(func):    # 闭包和装饰器的区别：闭包传递进来的是变量，装饰器传递进来的是函数
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间是 %s 秒" % (stop_time-start_time))
    return wrapper


@timer
def i_can_sleep():
    time.sleep(3)
    # return time.sleep(3)


print(timer(i_can_sleep()))
# start_time = time.time()
# i_can_sleep()   # 执行过成：num = timer(i_can_sleep())，num()
# stop_time = time.time()
# print('函数运行了 %s 秒' % (stop_time-start_time))









