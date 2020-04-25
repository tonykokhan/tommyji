print("step0")
try:
    print("step1")
    # a = 3 / 0
    a = 3 / 2
    print("step2")
except BaseException as e:
    print("step3")
    # print("发生异常，0不能做除数")
    print(e)
    print(type(e))

print("end!!!")
