# 【操作】csv.writer 对象写一个 csv 文件
import csv
headers = ["工号", "姓名", "年龄", "地址", "月薪"]
rows = [("1001", "高淇", 18, "西三旗 1 号院", "50000"),
        ("1002", "高八", 19, "西三旗 1 号院", "30000")]
with open(r"b.csv", "w") as b:
    b_csv = csv.writer(b)       # 创建 csv 对象
    b_csv.writerow(headers)     # 写入一行（标题）
    b_csv.writerows(rows)       # 写入多行（数据）

with open(r"b.csv", "r") as b:
    b_csv = csv.reader(b)
    for row in b_csv:
        print(row)
