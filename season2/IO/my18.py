# 【示例】实现递归的拷贝文件夹内容(使用 shutil 模块)
# 将文件夹“电影/学习”下面的内容拷贝到文件夹“音乐”下。拷贝时忽略所有的 html 和 htm 文件

import shutil

# "音乐"文件夹不存在才能用。
shutil.copytree(
    "电影/学习",
    "音乐",
    ignore=shutil.ignore_patterns(
        "*.html",
        "*.htm"))
