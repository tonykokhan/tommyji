# 【操作】使用迭代器（每次返回一行）读取文本文件
with open(r"e:\bb.txt", "r", encoding="utf-8") as f:
    for a in f:
        print(a)
        # print(a, end="")

