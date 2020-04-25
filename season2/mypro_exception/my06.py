# 读取文件，finally 中保证关闭文件资源

try:
    # f = open("f:/jikaiyuan.pem", 'r')
    f = open("f:/a.txt", 'r')
    content = f.readline()
    print(content)
# except BaseException as e:
#     print(e)
except:
    print("文件不存在")
finally:
    print("run in finally。关闭资源")
    try:
        f.close()   # 释放资源。此处也可能会发生异常，若发生异常，则程序终止，不会继续往下执行
    except BaseException as e:
        print(e)

print("程序执行结束！")
