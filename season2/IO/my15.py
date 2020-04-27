# 【示例】列出指定目录下所有的.py 文件，并输出文件名
import os
import os.path

path = os.getcwd()
print(path)
file_list = os.listdir(path)    # 列出子目录和子文件
print(file_list)

for filename in file_list:
    pos = filename.rfind(".")
    print(pos)
    print(filename[pos + 1:])
#     if filename[pos + 1:] == "py":
#         print(filename, end="\t")
#         print("##################")
#
# file_list2 = [filename for filename in os.listdir(path) if
#               filename.endswith(".py")]
#
# for filename in file_list2:
#     print(filename, end="\t")
