# LEGB规则
# Python在查找“名称”时，是按照LEGB规则查找的：Local --> Enclosed --> Global --> Built in。
# Local     指的就是函数或者类的方法内部
# Enclosed  指的是嵌套函数（一个函数包裹另一个函数，闭包）
# Global    指的是模块中的全局变量
# Built in  指的是Python为自己保留的特殊名称


# 测试LEGB规则


str = "global str"
# print(type(str))


def outer():

    # str = "outer"

    def inner():
        # str = "inner"
        print(str)

    inner()


outer()
