from pandas import Series, DataFrame
import pandas as pd

# obj = Series([4, 5, 6, -7])
# print(obj)
# print(obj.index)
# print(obj.values)
#
# # print({['a']: 1})

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])

print(obj2)

obj2['c'] = 6

print(obj2)

print('a' in obj2)
print('f' in obj2)


sdata = {
    'beijing': 35000,
    'shanghai': 71000,
    'guangzhou': 16000,
    'shenzhen': 5000}

obj3 = Series(sdata)
print(obj3)

obj3.index = ['bj', 'gz', 'sh', 'sz']

print(obj3)
