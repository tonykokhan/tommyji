# -*-coding:utf-8-*-

# 创建字典
d = {'name': 'cheng', 'age': 20, 'sex': 'female'}
print(d.keys())
print(d.values())
print(d['sex'])

# 创建空列表
a = []

# 将字典中键和值循环取出添加到列表中
for i in d.keys():
    a.append(i)
    a.append(d[i])
print(a)
