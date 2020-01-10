class Person:

    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.__age = age    # 私有属性，可以继承但是不能直接用

    def say_age(self):
        # print(self.name, "的年龄是：", self.age)
        print(self.name, "的年龄是：", self.__age)


class Student(Person):

    def __init__(self, name, age, score):
        self.score = score
        Person.__init__(self, name, age)    # 构造函数中包含调用父类构造函数。根据需要，不是必须。子类并不会自动调用父类的__init__()，我们必须显式的调用它。
        # self.name = name
        # self.age = age    # 这样写也可以，但不建议


p = Person("计开源", 18)
p.say_age()

s = Student("计开源", 18, 85)
s.say_age()
print(s.name)
# print(s.age)
print(s.score)
print(dir(s))
print(s._Person__age)
