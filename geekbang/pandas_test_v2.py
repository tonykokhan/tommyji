from pandas import Series, DataFrame
import pandas as pd

data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

# print(frame)
# print(frame2)
# print(frame2['city'])
# print(frame2.city)
# print(frame2.year)

frame2['new'] = 100
print(frame2)

frame2['cap'] = frame2.city == 'beijing'
print(frame2)

pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }

frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj5)

obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj6.reindex(range(6)))
print(obj6.reindex(range(6), method='ffill'))
print(obj6.reindex(range(6), method='bfill'))
