# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2019/12/11 16:58'


# . ^ $ * + ? {m} {m,n} {} \ \d \D \s ()
# ^$
# .*?

import re

p = re.compile('a')
print(p.match('a'))
print(p.match('b'))

p = re.compile('ca*t')
print(p.match('caat'))
print(p.match('caaat'))
print(p.match('caaaat'))


p = re.compile('.')
print(p.match('d'))

p = re.compile('..')
print(p.match('dd'))

p = re.compile('...')
print(p.match('ddd'))

p = re.compile('.{3}')
print(p.match('bat'))

# p = re.compile('....-..-..')
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-05-10').group(1))
# print(p.match('2018-05-10').group(2))
# print(p.match('2018-05-10').group(3))
# print(p.match('2018-05-10').groups())
#
# year, month, day = p.match('2018-05-10').groups()
# print(year)
# print(month)
# print(day)

# print(r'\nx\n')

print(p.search('aa2018-05-10bb'))

phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub('\D', '', phone)
print(p3)
