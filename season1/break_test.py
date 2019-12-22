# break语句可用于while和for循环，用来结束整个循环。当有嵌套循环时，break语句只能跳出最近一层的循环。

# 使用break语句结束循环
while True:
    a = input("请输入一个字符（输入Q或q结束）：")
    if a.upper() == 'Q':
        print("循环结束，退出")
        break
    else:
        print(a)


