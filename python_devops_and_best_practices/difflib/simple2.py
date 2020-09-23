# coding:utf8
# 生成美观的对比HTML格式文档
import difflib

text1 = """text1:	# 定义字符串1
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
and string
"""
text1_lines = text1.splitlines()  # 以行进行分隔，以便进行对比

text2 = """text2:	# 定义字符串2
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""
text2_lines = text2.splitlines()

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
