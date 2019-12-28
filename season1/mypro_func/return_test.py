# return返回值要点：
# 1. 如果函数体中包含return语句，则结束函数执行并返回值；
# 2. 如果函数体中不包含return语句，则返回None值；
# 3. 要返回多个返回值，使用列表、元组、字典、集合将多个值“存起来”即可。


# 定义一个打印n个星号的无返回值的函数
def print_star(n):
    print("*" * n)


print_star(5)


# 定义一个返回两个数平均值的函数
def my_avg(a, b):
    return (a + b) / 2


# 如下是函数的调用
c = my_avg(20, 30)
print(c)


# 测试返回值的基本用法
def add(a, b):
    print("计算两个数的和：{0}, {1}, {2}".format(a, b, (a + b)))
    return a + b


def test02():
    print("zhs")
    print("ji")
    return  # return两个作用：1. 返回值；2. 结束函数的执行
    print("hello")


def test03(x, y, z):
    return [x * 10, y * 10, z * 10]


c = add(30, 40)
print(add(30, 40) * 10)
d = test02()
print(d)
print(test03(4, 3, 2))
