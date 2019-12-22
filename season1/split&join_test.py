import time

a = "to be or not to be"

print(a.split())
print(a.split('be'))

a = ['six', 'six100', 'six200']
print('*'.join(a))
print('|'.join(a))
print(''.join(a))

# 拼接字符串要点：
# 使用字符串拼接符 +，会生成新的字符串对象，因此不推荐使用 + 来拼接字符串。推荐使用 join 函数，因为 join 函数在拼接字符串之前
# 会计算所有字符串的长度然后逐一拷贝，仅新建一次对象。


# 测试 + 拼接符和 join()，不同的效率
# join() 效率远高于 +
time01 = time.time()    # 起始时间
a = ""
for i in range(5000000):
    a += "sxt"

# print(a)

time02 = time.time()    # 终止时间
print("运算时间："+str(time02-time01))


time03 = time.time()
li = []
for i in range(5000000):
    li.append("sxt")

# print(li)
a = "".join(li)
# print(a)
time04 = time.time()
print("运算时间："+str(time04-time03))

# 输出：
# 运算时间：14.667612791061401
# 运算时间：0.8964188098907471


