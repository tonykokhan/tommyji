# map() 函数语法：
# map(function, iterable, ...)
# 参数
# function -- 函数
# iterable -- 一个或多个序列

# adict = {'a': 'aa', 'b': 'bb'}
#
#
# def func2(item):
#     return item[1]
#
#
# for i in adict.items():     # 取出字典中的每一个元素
#     print(i)
#     print(func2(i))


# filter()
# map()
# reduce()
# zip()

# a = [1, 2, 3, 4, 5, 6, 7]
# b = filter(lambda x: x >= 2, a)
# print(b)
# print(list(b))      # 强制转换成列表类型，否则lambda部分不会被执行


a = [1, 2, 3]
# aa = map(lambda x: x, a)     # 把多个参数依次进行处理。map()会根据提供的函数对指定序列做映射。
aa = map(lambda x: x+1, a)
print(aa)
print(list(aa))


b = [4, 5, 6]
print(list(map(lambda x, y: x+y, a, b)))




