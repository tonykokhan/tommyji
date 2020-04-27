# 【操作】csv.reader 对象于从 csv 文件读取数据
import csv
with open(r"a.csv") as a:
    a_csv = csv.reader(a)   # 创建 csv 对象，它是一个包含所有数据的列表，每一行为一个元素
    print(next(a_csv))
    headers = next(a_csv)   # 获得列表对象，包含标题行的信息
    print(headers)
    for row in a_csv:       # 循环打印各行内容
        print(row)
