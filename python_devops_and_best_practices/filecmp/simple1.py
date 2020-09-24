# -*- coding: utf-8 -*-
__author__ = 'tommyji'
__date__ = '2020/9/24 9:46'

# 对比dir1与dir2的目录差异
# coding:utf8
import filecmp

a = "E:\\PycharmProjects\\tommyji\python_devops_and_best_practices\\filecmp\\dir1"  # 定义左目录
b = "E:\\PycharmProjects\\tommyji\python_devops_and_best_practices\\filecmp\\dir2"  # 定义右目录

dirobj = filecmp.dircmp(a, b, ['test.py'])  # 目录比较，忽略test.py文件。cmp（单文件对比）、cmpfiles（多文件对比）、dircmp（目录对比）
fileobj = filecmp.cmpfiles(a, b, ['abc', 'aaa', 'a.log', 'test.txt', 'test1.txt'])            # 多文件对比

# 输出对比结果数据报表，详细说明请参考filecmp类方法及属性信息
dirobj.report()                     # 比较当前指定目录中的内容
dirobj.report_partial_closure()     # 比较当前指定目录及第一级子目录中的内容
dirobj.report_full_closure()        # 递归比较所有指定目录的内容

print(fileobj)  # (['a.log'], ['abc'], ['aaa', 'test.txt', 'test1.txt'])，分别对应：匹配、不匹配、错误

print("left_list:" + str(dirobj.left_list))             # 左目录中的文件及目录列表
print("right_list:" + str(dirobj.right_list))           # 右目录中的文件及目录列表
print("common:" + str(dirobj.common))                   # 两边目录共同存在的文件或目录
print("left_only:" + str(dirobj.left_only))             # 只在左目录中的文件或目录
print("right_only:" + str(dirobj.right_only))           # 只在右目录中的文件或目录
print("common_dirs:" + str(dirobj.common_dirs))         # 两边目录都存在的子目录
print("common_files:" + str(dirobj.common_files))       # 两边目录都存在的子文件
print("common_funny:" + str(dirobj.common_funny))       # 两边目录都存在的子目录（不同目录类型或os.stat()记录的错误）
print("same_file:" + str(dirobj.same_files))            # 匹配相同的文件
print("diff_files:" + str(dirobj.diff_files))           # 不匹配相同的文件？
print("funny_files:" + str(dirobj.funny_files))         # 两边目录中都存在，但无法比较的文件
