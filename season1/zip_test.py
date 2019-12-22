# 使用zip()并行迭代：
# 我们可以通过zip()函数对多个序列进行并行迭代，zip()函数在最短序列“用完”时就会停止。

# 测试zip()并行迭代
names = ("计开源", "计老二", "计老三", "计老四")
ages = (18, 16, 20, 25)
jobs = ("老师", "程序员", "公务员")

for name, age, job in zip(names, ages, jobs):
    print("{0}-{1}-{2}".format(name, age, job))

for i in range(3):
    print("{0}-{1}-{2}".format(names[i], ages[i], jobs[i]))
