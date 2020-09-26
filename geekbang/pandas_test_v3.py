from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA

data = Series([1, NA, 2])
# print(data)
# print(data.dropna())

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])

# print(data2.dropna())
# print(data2.dropna(how='all'))

data2[4] = NA
# print(data2)    # 删除前
# print(data2.dropna(axis=1, how='all'))  # 删除后，axis=1代表的是列

data2.fillna(0)
# print(data2)
# print(data2.fillna(0))
print(data2.fillna(0, inplace=True))
print(data2)


# 层次化索引
data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

# print(data3)
# print(data3['b': 'c'])
print(data3.unstack())  # 转换成二维数据
print(data3.unstack().stack())  # 再转换回来
