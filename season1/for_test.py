# for循环和可迭代对象遍历：
# for循环通常用于可迭代对象的遍历

# 可迭代对象：
# 1. 序列。包含：字符串、列表、元组
# 2. 字典
# 3. 迭代器对象(iterator)
# 4. 生成器函数(generator)

for x in (20, 30, 40):
    print(x * 3)


# 遍历字符串中的字符
a = list("zhs001")
print(a)
for x in list("zhs001"):
    print(x)

for x in "zhs001":
    print(x)


# 遍历字典
a = {'name': 'tommyji', 'age': 18, 'address': '科汇大厦10楼'}
for x in a:     # 遍历字典所有的key
    print(x)

for x in a.keys():  # 遍历字典所有的key
    print(x)

for x in a.values():    # 遍历字典所有的value
    print(x)

for x in a.items():     # 遍历字典所有的“键值对”
    print(x)


# 嵌套循环：
# 一个循环体内可以嵌入另一个循环，一般称为“嵌套循环”，或者“多重循环”
# for x in range(5):
#     print(x)
#     print()

for x in range(5):
    for y in range(5):  # 循环5次
        print(x, end="\t")
    print()     # 起到换行的作用


# 利用嵌套循环打印九九乘法表
for m in range(1, 10):
    for n in range(1, m + 1):
        print("{0}*{1}={2}".format(m, n, (m * n)), end="\t")
    print()     # 换行


# 使用列表和字典存储表格的数据
r1 = dict(name="计小一", age=18, salary=30000, city="北京")
r2 = dict(name="计小二", age=19, salary=20000, city="上海")
r3 = dict(name="计小五", age=20, salary=10000, city="深圳")
tb = [r1, r2, r3]

for x in tb:
    if x.get("salary") > 15000:
        print(x)
