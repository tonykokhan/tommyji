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
# # b = map(lambda x: x, a)
# b = map(lambda x: x+1, a)
# print(b)
# print(list(b))


b = [4, 5, 6]
print(list(map(lambda x, y: x+y, a, b)))




