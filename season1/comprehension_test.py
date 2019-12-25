# 推导式创建序列：
# 推导式是从一个或者多个迭代器快速创建序列的一种方法。它可以将循环和条件判断结合，从而避免冗长的代码。
# 推导式是典型的Python风格，会使用它代表你已经超过Python初学者的水平。

# 1. 列表推导式
a = [x for x in range(1, 5)]
print(a)

a = [x * 2 for x in range(1, 5)]
print(a)

a = [x * 2 for x in range(1, 20)]
print(a)

a = [x * 2 for x in range(1, 20) if x % 5 == 0]
print(a)

a = [a for a in "abcdefg"]
print(a)

cells = [(row, col) for row in range(1, 10)
         for col in range(1, 10)]    # 可以使用两个循环
print(cells)


# 2. 字典推导式
# 字典的推导式生成字典对象，格式如下：
# {key_expression: value_expression for item in 可迭代对象}
# 类似于列表推导式，字典推导式也可以增加if条件判断、多个for循环
# 统计文本中字符出现的次数：
my_text = 'i love jikaiyuan, i love tommyji, i love tonykokhan, i love sai'
chart_count = {c: my_text.count(c) for c in my_text}
print(chart_count)


# 3. 集合推导式
# 集合推导式生成集合，和列表推导式的语法格式类似：
# {表达式 for item in 可迭代对象}
# 或者
# {表达式 for item in 可迭代对象 if 条件判断}
a = {x for x in range(1, 100) if x % 9 == 0}
print(a)


# 4. 生成器推导式（生成元组）
gnt = (x for x in range(1, 100) if x % 9 == 0)
print(gnt)
# <generator object <genexpr> at 0x000002505C982970>    # 提示的是“一个生成器对象”。显然，元组是没有推导式的

print(tuple(gnt))
print(tuple(gnt))   # 一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了
# 或
for x in gnt:
    print(x, end=' ')
for x in gnt:
    print(x, end=' ')   # 一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了

