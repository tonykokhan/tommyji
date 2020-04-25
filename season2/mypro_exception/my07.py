# return 语句和异常处理问题


def test01():
    print("step1")
    try:
        x = 3 / 0
        # return "a"
    except:
        print("step2")
        print("异常，0不能做除数")
        # return "b"
    finally:
        print("step3")
        # return "d"

    print("step4")
    return "e"  # 一般不要将return语句放到try、except、else、finally块中，会发生一些意想不到的错误，建议放到方法最后。


print(test01())
