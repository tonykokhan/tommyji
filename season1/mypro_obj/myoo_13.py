# 类成员的继承和重写
# 1. 成员继承：子类继承了父类除构造方法之外的所有成员。
# 2. 方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为“重写”


# 继承和重写的案例
class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def say_age(self):
        print("我的年龄：", self.__age)
        # print("我的年龄：{0}".format(self.__age))

    def say_introduce(self):
        print("我的名字：{0}".format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)    # 必须显式的调用父类初始化方法，不然解释器不会去调用
        self.score = score

    def say_introduce(self):
        """
        重写了父类方法
        """
        print("报告老师，我的名字是：{0}".format(self.name))


s = Student("计开源", 18, 80)
s.say_age()
s.say_introduce()
