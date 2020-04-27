# 【示例】seek()移动文件指针示例
with open("e.txt", "r", encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    # print(str(f.readlines()))   # readlines() 文本文件中，每一行作为一个字符串存入列表中，返回该列表
    print("读取的内容：{0}".format(str(f.readlines())))
    print(f.tell())     # tell() 返回文件指针的当前位置
    f.seek(0, 0)
    # print(f.tell())
    print("读取的内容：{0}".format(str(f.readlines())))

