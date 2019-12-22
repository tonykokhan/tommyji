# 字典：
# 字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值对”，包含：“键对象”和“值对象”。
# 可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。


# 我们可以通过{}、dict()来创建字典对象
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
print(a)

b = dict(name='tommyji', age=18, job='programmer')
print(b)

c = dict([('name', 'tommyji'), ('age', 18), ('job', 'programmer')])
print(c)

d = {}  # 空的字典对象
print(d)

e = dict()  # 空的字典对象
print(e)


# 通过zip()创建字典对象
k = ['name', 'age', 'job']
v = ['tommyji', 18, 'teacher']
d = dict(zip(k, v))
print(d)


# 通过fromkeys创建值为空的字典
a = dict.fromkeys(['name', 'age', 'job'])
print(a)


# 字典元素的访问：
# 1. 通过[键]获得“值”。若键不存在，则抛出异常。
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
print(a['name'])
print(a['age'])
# print(a['sex'])     # 键不存在，报错

# 2. 通过get()方法获得“值”，推荐使用。优点是：指定键不存在，返回None；也可以设定指定键不存在时默认返回的对象。
# 推荐使用get()获取“值对象”。
print(a.get('name'))
print(a.get('sex'))
print(a.get('sex', '一个男人'))

# 3. 列出所有的键值对
print(a.items())

# 4. 列出所有的键，列出所有的值
print(a.keys())
print(a.values())

# 5. len()键值对的个数
print(len(a))

# 6. 检测一个“键”是否在字典中
a = {'name': 'tommyji', 'age': 18}
print('name' in a)
print('age' in a)


# 字典元素添加、修改、删除
# 1. 给字典新增“键值对”。如果“键”已经存在，则覆盖旧的键值对；如果“键”不存在，则新增“键值对”。
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
a['address'] = '疏影路711弄'
a['age'] = 16
print(a)

# 2. 使用update()将新字典中所有键值对全部添加到旧字典对象上。如果key有重复，则直接覆盖。
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
b = {'name': 'tonykokhan', 'money': 1000, 'sex': '男的'}
a.update(b)
print(a)

# 3. 字典中元素的删除，可以使用del()方法；或者clear()删除所有键值对；pop()删除指定键值对，并返回对应的“值对象”
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
del(a['name'])
print(a)
b = a.pop('age')
print(b)
a.clear()
print(a)

# 4. popitem()：随机删除和返回该键值对。字典是“无序可变序列”，因此没有第一个元素、最后一个元素的概念；popitem弹出随机的项，
# 因为字典并没有“最后的元素”或者其他有关顺序的概念。若想一个接一个地移除并处理项，这个方法就非常有效（因为不用首先获取键的列表）
a = {'name': 'tommyji', 'age': 18, 'job': 'programmer'}
a.popitem()
print(a)
a.popitem()
print(a)
a.popitem()
print(a)


# 序列解包：
# 序列解包可以用于元组、列表、字典，序列解包可以让我们方便的对多个变量赋值。
x, y, z = (20, 30, 10)
print(x)
print(y)
print(z)

(a, b, c) = (9, 8, 10)
print(a)
print(b)
print(c)

[a, b, c] = [10, 20, 30]
print(a)
print(b)
print(c)

# 序列解包用于字典时，默认是对“键”进行操作；如果需要对键值对操作，则需要使用items()；如果需要对“值”进行操作，则需要使用values();
s = {'name': 'tommyji', 'age': 18, 'job': 'teacher'}
name, age, job = s  # 默认对键进行操作
print(name)
name, age, job = s.items()  # 对键值对进行操作
print(name)
name, age, job = s.values()     # 对值进行操作
print(name)
