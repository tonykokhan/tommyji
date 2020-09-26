# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/11 16:01'


class Testwith():
    def __enter__(self):
        print('run')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s' % exc_tb)


with Testwith():
    print('Test is running')
    raise NameError('testNameError')

