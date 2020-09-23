# coding:utf8
import difflib
import sys

try:
    textfile1 = sys.argv[1]  # 第一个配置文件路径参数
    # print(textfile1)
    textfile2 = sys.argv[2]  # 第二个配置文件路径参数
    # print(textfile2)
except Exception as e:
    print("Error:" + str(e))
    print("Usage1: simple3.py filename1 filename2")
    sys.exit()


def readfile(filename):  # 文件读取分隔函数
    try:
        fileHandle = open(filename, 'rb')
        string = fileHandle.read().decode()    # python3为字节，python2为字符串。需要将字节转换为字符串，参考：https://blog.csdn.net/cunchi4221/article/details/107475824
        text = string.splitlines()  # 读取字符串后以行进行分隔，然后放到一个列表里
        print(text)
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()


if textfile1 == "" or textfile2 == "":
    print("Usage2: simple3.py filename1 filename2")
    sys.exit()

text1_lines = readfile(textfile1)			# 调用readfile函数，获取分隔后的字符串
# print(text1_lines)
text2_lines = readfile(textfile2)
# print(text2_lines)

d = difflib.HtmlDiff()				# 创建HtmlDiff()类对象
print(d.make_file(text1_lines, text2_lines))
# print(d.make_file(text1_lines, text2_lines))  # 通过make_file方法输出HTML格式的比对结果
