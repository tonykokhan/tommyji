class Student:  # 类名一般首字母大写，多个单词采用驼峰原则

    def __init__(self, name, score):     # self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):    # self必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name, self.score))


s1 = Student("计开源", 60)
s1.say_score()
print(s1.name)
print(s1.score)

s1.age = 18
s1.salary = 3000
# del s1
print(s1.salary)
print(dir(s1))

s2 = Student("计小开", 100)
print(s2.name)
print(s2.score)
s2.say_score()
Student.say_score(s2)   # 解释器实际调用情况，同上，效果一模一样

print(dir(s2))
print(s2.__dict__)
print(isinstance(s2, Student))


class Man:
    pass


print(isinstance(s2, Man))
