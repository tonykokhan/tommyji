from functools import reduce

a = reduce(lambda x, y: x + y, [2, 3, 4], 1)
print(a)

# 效果：((1+2)+3)+4

a = zip((1, 2, 3), (4, 5, 6))
# print(a)
for i in a:
    print(i)

# 效果：类似数学中的矩阵变换
# (1, 2, 3)
# (4, 5, 6)
#
# (1, 4)
# (2, 5)
# (3, 6)

dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dicta.values())
print(dicta.keys())
# print(dicta.items())
print(dict(dictb))  # 转换成字典
