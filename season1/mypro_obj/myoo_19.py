# super()获取父类定义
# 在子类中，如果想要获得父类的方法时，我们可以通过super()来做。
# super()代表父类的定义，不是父类对象。


# 测试super()，代表父类的定义，而不是父类的对象
class A:

    def say(self):
        print("A:", self)


class B(A):

    def say(self):
        # A().say()
        # A.say(self)         # 另一种方式，效果同 super().say()
        super().say()       # 获得父类的方法
        print("B:", self)


# A().say()
# print(B.mro())
B().say()
