# 【操作】为文本文件每一行的末尾增加行号
with open(r"e:\bb.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    lines = [line.rstrip() + "#" +
             str(index + 1) + "\n" for index, line in enumerate(lines)]     # 推导式生成列表
    print(lines)

with open(r"e:\bb.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
