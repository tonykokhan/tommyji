# num = input("输入一个数字：")
#
# if int(num) < 10:
#     print(num)
# else:
#     print("数字太大")

# 三元条件运算符
num = input("请输入一个数字")
print(num if int(num) < 10 else "数字太大")     # 可以看到，这种写法更加简洁，易读
