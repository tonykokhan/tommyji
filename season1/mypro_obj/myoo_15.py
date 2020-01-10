# 查看对象所有属性以及和object进行比对
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.age)


obj = object()
print(dir(obj))

s = Person("计开源", 18)
print(dir(s))
print(s.name)
print(s.age)
print(s.say_age)    # 发现say_age显然是方法，实际上也是属性
print(type(s.name))
print(type(s.age))
print(type(s.say_age))  # 只不过，这个属性的类型是“method”而已


# 从上面我们可以发现这样几个要点：
# 1. Person对象增加了六个属性：
# __dict__, __module__, __weakref__, age, name, say_age
#
# 2. object的所有属性，Person类作为object的子类，显然包含了所有的属性。
#
# 3. 我们打印age、name、say_age，发现say_age显然是方法，实际上也是属性。只不过，这个属性的类型是“method”而已。
# age       <class 'int'>
# name      <class 'str'>
# say_age   <class 'method'>
