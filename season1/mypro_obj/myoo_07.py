# 方法没有重载：
#
# 在其他语言中，可以定义多个重名的方法，只要保证方法签名唯一即可。方法签名包含3个部分：方法名、参数数量、参数类型。
#
# 在Python中，方法的参数没有声明类型（调用时确定参数的类型），参数的数量也可以由可变参数控制。因此，Python中是没有
# 方法的重载的。定义一个方法即可有多种调用方式，相当于实现了其他语言中的方法的重载。
#
# 如果我们在类体中定义了多个重名的方法，只有最后一个方法有效。
#
# 建议：不要使用重名的方法！Python中方法没有重载。


# Python中没有方法的重载。定义多个同名方法，只有最后一个有效
class Person:

    def say_hi(self):
        print("hello")

    def say_hi(self, name):
        print("{0}, hello".format(name))


p1 = Person()
# p1.say_hi()   # 不带参，报错：TypeError: say_hi() missing 1 required positional argument: 'name'
p1.say_hi("计开源")    # 定义多个同名方法，只有最后一个有效
