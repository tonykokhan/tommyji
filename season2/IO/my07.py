# 【操作】 读取图片文件，实现文件的拷贝
with open("ubuntu.png", "rb") as f:
    with open("ubuntu_copy.png", "wb") as w:
        for line in f.readlines():
            print(line)
            # w.write(line)
print("图片拷贝完成！")
