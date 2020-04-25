# 测试with上下文管理器（with不是用来取代try...except...finally结构的，只是作为补充。方便我们在文件管理、网络通信时的开发）

with open("f:/jikaiyuan.pem", "r") as f:
    content = f.readline()
    print(content)

print("程序执行结束！")
