# 测试traceback模块的使用

import traceback

# try:
#     print("step1")
#     num = 1 / 0
# except:
#     traceback.print_exc()


############# 将异常信息写入到指定的文件中 ##############
try:
    print("step1")
    num = 1 / 0
except:
    with open("f:/a.txt", "a") as f:
        traceback.print_exc(file=f)
