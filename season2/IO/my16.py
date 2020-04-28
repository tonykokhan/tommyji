# 【示例】使用 walk()递归遍历所有文件和目录
import os

all_files = []

path = os.getcwd()
print(path)
list_files = os.walk(path)
# print(list_files)
# print(type(list_files))
# print(tuple(list_files))
# tuple(list_files)

for dirpath, dirnames, filenames in list_files:
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    for dir in dirnames:
        # print(dir)
        all_files.append(os.path.join(dirpath, dir))
        # print("############")
        # print(all_files)
    for name in filenames:
        # print(name)
        all_files.append(os.path.join(dirpath, name))
        # print("###############")
        # print(all_files)

for file in all_files:
    print(file)
