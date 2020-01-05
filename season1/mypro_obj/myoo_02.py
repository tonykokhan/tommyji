# 类属性的使用测试


class Student:

    company = "ZHS"     # 类属性
    count = 0           # 类属性

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):    # 实例方法
        print("我的公司是：", Student.company)
        print(self.name, '的分数是：', self.score)


s1 = Student('张三', 80)      # s1是实例对象，自动调用__init__()方法
s1.say_score()
print('一共创建{0}个Student对象'.format(Student.count))
