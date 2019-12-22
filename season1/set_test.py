# 集合：
# 集合是无序可变的，元素不能重复。实际上，集合底层是字典实现，集合的所有元素都是字典中的“键对象”，因此是不能重复的且唯一的。


# 集合创建和删除
# 使用{}创建集合对象，并使用add()方法添加元素
a = {3, 5, 7}
print(a)

a.add(9)
print(a.add(9))
print(a)

# 使用set()，将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保留一个。
a = ['a', 'b', 'c', 'd']
b = set(a)
print(b)
print(set(a))

# remove()删除指定元素；clear()清空整个集合
a = {10, 20, 30, 40, 50}
a.remove(20)
print(a)
a.clear()
print(a)


# 集合相关操作：
# 像数学中概念一样，Python对集合也提供了并集、交集、差集等运算
a = {1, 3, 'zhs'}
b = {'he', 'it', 'zhs'}
print(a | b)    # 并集
print(a & b)    # 交集
print(a - b)    # 差集

print(a.union(b))           # 并集
print(a.intersection(b))    # 交集
print(a.difference(b))      # 差集
