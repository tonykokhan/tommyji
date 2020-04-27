# 【操作】按行读取一个文件
with open(r"e:\bb.txt", "r", encoding="utf-8") as f:
    while True:
        fragment = f.readline()     # 读取一行内容作为结果返回。读取到文件末尾，会返回空字符串。
        if not fragment:
            break
        else:
            print(fragment)
            # print(fragment, end="")


