# 递归函数
# 递归函数指的是：自己调用自己的函数，在函数体内部直接或间接的自己调用自己。

# 每个递归函数必须包含两个部分：
# 1. 终止条件
# 表示递归什么时候结束。一般用于返回值，不再调用自己。
# 2. 递归步骤
# 把第n步的值和第n-1步相关联。


# 使用递归函数计算阶乘(factorial)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


for i in range(1, 6):
    print(i, "!=", factorial(i))

factorial(6)


# 测试递归函数的基本原理
def test01(n):
    print("test01:", n)
    if n == 0:
        print("over")
    else:
        test01(n-1)
    print("test01***", n)


test01(4)
