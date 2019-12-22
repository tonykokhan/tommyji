# 循环代码优化测试
import time

start = time.time()
for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i * 1000 + m * 1000)

end = time.time()
print("耗时：{0}".format(end - start))

start2 = time.time()
for i in range(1000):
    result = []
    c = i * 1000
    for m in range(10000):
        result.append(c + m * 100)

end2 = time.time()
print("耗时：{0}".format(end2 - start2))


# 循环代码优化：
# 1. 尽量减少循环内部不必要的计算
# 2. 嵌套循环中，尽量减少内层循环的计算，尽可能向外提
# 3. 局部变量查询较快，尽量使用局部变量

# 其他优化手段：
# 1. 连接多个字符串，使用join()而不使用+
# 2. 列表进行元素插入和删除，尽量在列表尾部操作
