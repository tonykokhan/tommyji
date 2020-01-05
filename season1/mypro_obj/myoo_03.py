# 类方法使用测试
class Student:
    company = "ZHS"     # 类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)


Student.printCompany()
