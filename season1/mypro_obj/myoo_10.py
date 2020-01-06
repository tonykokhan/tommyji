# @property装饰器
# @property可以将一个方法的调用方式变成“属性调用”。下面是一个简单的示例，让大家体会一下这种转变：

# 简单测试@property


class Employee:

    @property
    def salary(self):
        return 30000


emp1 = Employee()
print(emp1.salary)          # 打印30000
print(type(emp1.salary))    # 打印<class 'int'>
# emp1.salary()             # 报错：TypeError: 'int' object is not callable

# emp1.salary = 1000          # @property修饰的属性，如果没有加setter方法，则为只读属性。此处修改报错：AttributeError: can't set attribute
