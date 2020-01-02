# 嵌套函数（内部函数）
# 在函数内部定义的函数！


# 嵌套函数定义
def f1():
    print('f1 running...')

    def f2():
        print('f2 running...')

    f2()


f1()

# 执行结果：
# f1 running...
# f2 running...

# 上面程序中，f2()就是定义在f1函数内部的函数。f2()的定义和调用都在f1()函数内部。
