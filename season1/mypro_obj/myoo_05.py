# 析构函数
class Person:

    def __del__(self):
        print("被销毁对象：{0}".format(self))


p1 = Person()
p2 = Person()
del p2
print("结束程序")
print(p1)
# print(p2)
