# 模块是在代码量变得相当大之后，为了将需要重复使用的有组织的代码段放在一起，
# 这部分代码可以附加到现有的程序中，附加的过程叫做导入(import)
# 导入模块的一般写法：
# import 模块名称
# from 模块名称 import 方法名


def print_me():
    print('me')


# print_me()


# PEP8规范：
# 文档：
# https://www.python.org/dev/peps/pep-0008/
# 安装：
# pip install autopep8
# PyCharm配置：
# Name: autopep8
# Program: autopep8
# Arguments: --in-place --aggressive --aggressive $FilePath$
# Working directory: $ProjectFileDir$
# Output filters: $FILE_PATH$\:$LINE$\:$COLUMN$\:.*

