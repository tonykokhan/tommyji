# 元组tuple
# 列表属于可变序列，可以任意修改列表中的元素。元组属于不可变序列，不能修改元组中的元素。
# 因此，元组没有增加元素、修改元素、删除元素相关的方法。

# 元组支持如下操作：
# 1. 索引访问
# 2. 切片操作
# 3. 连接操作
# 4. 成员关系操作
# 5. 比较运算操作
# 6. 计数：元组长度len()、最大值max()、最小值min()、求和sum()等

# a = (10, 20, 30)
a = 10, 20, 30  # 如果元组只有一个元素，则必须后面加逗号。这是因为解释器会把(1)解释为整数1，把(1,)解释为元组。
print(a)


# 通过tuple()创建元组
# tuple(可迭代的对象)

b = tuple   # 创建一个空元组对象
print(b)
b = tuple("abc")
print(b)
b = tuple(range(3))
print(b)
b = tuple([2, 3, 4])
print(b)


# 总结：
# tuple()可以接收列表、字符串、其他序列类型、迭代器等生成元组
# list()可以接收元组、字符串、其他序列类型、迭代器等生成列表


# 列表关于排序的方法list.sorted()是修改原列表对象，元组没有该方法。
# 如果要对元组排序，只能使用内置函数sorted(tupleObj)，并生成新的列表对象（注意这里是列表对象）


# zip(列表1, 列表2, ...)将多个列表对应位置的元素组合成为元组，并返回这个zip对象
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90]
d = zip(a, b, c)
print(d)
# print(tuple(d))
print(list(d))


# 生成器推导式创建元组：
# 从形式上看，生成器推导式与列表推导式类似，只是生成器推导式使用小括号。列表推导式直接生成列表对象，生成器推导式生成的不是列表也不是元组，
# 而是一个生成器对象。
# 我们可以通过生成器对象，转化成列表或者元组。
# 也可以使用生成器对象__next__()方法进行遍历，或者直接作为迭代器对象来使用。
# 不管什么方式使用，元素访问结束后，如果需要重新访问其中的元素，必须重新创建该生成器对象。

s = (x*2 for x in range(5))
print(s)
print(tuple(s))
print(list(s))  # 只能访问一次元素，第二次就为空了，需要再生成一次
print(s)
print(tuple(s))

s = (x*2 for x in range(5))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())


# 元组总结：
# 1. 元组的核心特点是：不可变序列
# 2. 元组的访问和处理速度比列表快
# 3. 与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键使用