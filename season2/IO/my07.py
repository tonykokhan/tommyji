# 【操作】 读取图片文件，实现文件的拷贝
with open("ubuntu.png", "rb") as f:
    with open("ubuntu_copy.png", "wb") as w:
        for line in f.readlines():  # readlines() 文本文件中，每一行作为一个字符串存入列表中，返回该列表
            # print(line)
            w.write(line)
print("图片拷贝完成！")
