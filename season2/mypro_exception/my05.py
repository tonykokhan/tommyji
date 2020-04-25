# try...except...finally结构中，finally无论是否发生异常都会被执行：通常用来释放try块中申请的资源。

try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print(c)
finally:
    print("我是finally中的语句，无论发生异常与否，都执行！")

print("程序结束")
