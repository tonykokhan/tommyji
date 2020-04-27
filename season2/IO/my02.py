try:
    f = open(r"my01.txt", "a")
    str = "tommyji"
    f.write(str)
except BaseException as e:
    print(e)
finally:
    f.close()
