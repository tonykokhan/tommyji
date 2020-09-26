# -*- coding: utf-8 -*-
def new_tips(argv):
    def tips(func):
        def wrapper(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')
        return wrapper
    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('sub_module')
def sub(a, b):
    print(a - b)


# add(4, 5)
print(add(4, 5))  # None由此返回
# print(sub(7, 3))
