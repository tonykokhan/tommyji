# 【示例】使用递归算法遍历目录下所有文件
import os
allfile = []


def getFiles(path, level):
    childFiles = os.listdir(path)
    # print(childFiles)
    for file in childFiles:
        # print(file)
        filepath = os.path.join(path, file)
        # print(filepath)
    if os.path.isdir(filepath):
        getFiles(filepath, level + 1)
    # allfile.append("\t" * level + filepath)
    allfile.append(filepath)
    print(allfile)


getFiles(os.getcwd(), 0)

for f in reversed(allfile):
    print(f)
