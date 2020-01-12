# 测试单例模式
class MySingleton:

    __obj = None    # 定义类的私有属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init...")
            self.name = name
            MySingleton.__init_flag = False


a = MySingleton("aa")
b = MySingleton("bb")
print(dir(MySingleton))
print(dir(a))
print(a)
print(a._MySingleton__obj)  # 同 print(a)
print(a._MySingleton__init_flag)    # False
print(b)
print(b._MySingleton__obj)  # 同 print(b)
print(b._MySingleton__init_flag)    # False
c = MySingleton("cc")
print(c)
print(c._MySingleton__obj)  # 同 print(c)
print(c._MySingleton__init_flag)    # False
print(a.name)   # aa
print(b.name)   # aa
print(c.name)   # aa
