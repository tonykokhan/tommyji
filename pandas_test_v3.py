from pandas import Series, DataFrame
import pandas as pd
from numpy import nan as NA

data = Series([1, NA, 2])
print(data)
# print(data.dropna())

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])

print(data2.dropna())
print(data2.dropna(how='all'))

data2[4] = NA
print(data2)
print(data2.dropna(axis=1, how='all'))

data2.fillna(0)
print(data2.fillna(0, inplace=True))
print(data2)

