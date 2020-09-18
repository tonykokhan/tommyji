# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/5 15:52'

# i = j

# print())

# a = '123'
# print(a[3])

# d = {'a': 1, 'b': 2}
# print(d['a'])
# print(d['c'])

# year = int(input('input year: '))

# try:
#     year = int(input('input year: '))
# except ValueError:
#     print('年份要输入数字')

# a = '123'
# a.append()

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能做除数 %s' % e)

# try:
#     print(1/0)
# except Exception as e:
#     print(e)

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

# try:
#     raise ValueError('helloError')
# except ValueError:
#     print('my custom error')

try:
    # a = open('name.txt')
    a = open('name1.txt')
except Exception as e:
    print(e)

# finally:
#     a.close()

