# 使用嵌套函数避免重复代码
def printChineseName(name, familyName):
    print("{0} {1}".format(familyName, name))   # 先打姓，后打名


def printEnglishName(name, familyName):
    print("{0} {1}".format(name, familyName))   # 先打名，后打姓


def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print("{0} {1}".format(a, b))
    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)


printChineseName("小开", "计")
printEnglishName("tommy", "ji")
printName(True, "小开", "计")
printName(False, "小开", "计")
