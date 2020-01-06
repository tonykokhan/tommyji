# @property装饰器的用法
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("计开源", 30000)
print(emp1.salary)
emp1.salary = -20000
print(emp1.salary)
