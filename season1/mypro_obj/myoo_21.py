# 测试运算符的重载
class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            # print(other)
            # print(Person)
            # print(self.name)
            # print(other.name)
            return "{0}--{1}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other, int):
            print(other)    # 3
            return self.name * other
        else:
            return "不是同类对象，不能相乘"


p1 = Person("计开源")
p2 = Person("计小开")

# p1 + p2   # 调用__add__()方法
x = p1 + p2
print(x)    # 打印函数的返回值。计开源--计小开
# print(x * 3)
# print(p1 * 3)
print(p2 * 3)   # 计小开计小开计小开
