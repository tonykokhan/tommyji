# MRO()
# Python支持多继承，如果父类中有相同名字的方法，在子类没有指定父类名时，解释器将“从左向右”按顺序搜索。
# MRO(Method Resolution Order)：方法解析顺序。我们可以通过mro()方法获得“类的层次结构”，方法解析顺序也是按照这个“类的层次结构”寻找的。


# 多重继承


class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAA!")


class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB!")


class C(B, A):
    def cc(self):
        print("cc")


# class C(A, B):
#     def cc(self):
#         print("cc")


c = C()
# c.cc()
# c.bb()
# c.aa()
print(C.mro())  # 打印类的层次结构：[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
c.say()         # 解释器寻找方法是“从左到右”的方式寻找，此时会执行B类中的say()
