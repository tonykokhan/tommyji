# 【示例】测试 os.path 中常用方法
import os
import os.path

# 获得目录、文件基本信息
print(os.path.isabs("e:/bb.txt"))       # 是否绝对路径
print(os.path.isdir("e:/bb.txt"))       # 是否目录
print(os.path.isfile("e:/bb.txt"))      # 是否文件
print(os.path.exists("a.txt"))          # 文件是否存在
print(os.path.getsize("e.txt"))         # 文件大小
print(os.path.abspath("e.txt"))         # 输出绝对路径
print(os.path.dirname("e:/bb.txt"))     # 输出所在目录

# 获得创建时间、访问时间、最后修改时间
print(os.path.getctime("e.txt"))        # 返回创建时间
print(os.path.getatime("e.txt"))        # 返回最后访问时间
print(os.path.getmtime("e.txt"))        # 返回最后修改时间

# 对路径进行分割、连接操作
path = os.path.abspath("a.txt")         # 返回绝对路径
print(os.path.split(path))              # 返回元组：目录、文件
# ('C:\\Users\\Administrator\\PycharmProjects\\mypro_io\\test_os', 'a.txt')
print(os.path.splitext(path))           # 返回元组：路径、扩展名
# ('C:\\Users\\Administrator\\PycharmProjects\\mypro_io\\test_os\\a', '.txt')
print(os.path.join("aa", "bb", "cc"))   # 返回路径：aa/bb/cc(linux); aa\bb\cc(windows)
