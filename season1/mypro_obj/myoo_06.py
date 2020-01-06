# __call__方法和可调用对象
# 定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用。


# 测试可调用方法__call__()
class SalaryAccount:
    """工资计算类"""

    def __call__(self, salary):
        print("算工资啦...")
        yearSalary = salary*12
        daySalary = salary//22.5    # 国家规定的每个月的平均工作天数
        hourSalary = daySalary//8

        return dict(yearSalary=yearSalary, monthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(300000))

