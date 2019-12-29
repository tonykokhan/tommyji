# 浅拷贝和深拷贝：
# 浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用（即父对象）
# 深拷贝：会连子对象的内容也全部拷贝一份，对子对象的修改不会影响源对象

# python中的对象之间赋值时是按引用传送的，如果需要拷贝对象，需要使用标准库中的copy模块
# 1、copy.copy 浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象。（子对象（数组）修改，也会修改）
# 2、copy.deepcopy 深拷贝，拷贝对象及其子对象（原始对象）

# 测试浅拷贝、深拷贝

import copy


def testCopy():
    """
    测试浅拷贝
    """
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print("a:", a)
    print("b:", b)

    b.append(30)
    b[2].append(7)
    print("浅拷贝......")
    print("a:", a)
    print("b:", b)


def testDeepCopy():
    """
    测试深拷贝
    """
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print("a:", a)
    print("b:", b)

    b.append(30)
    b[2].append(7)
    print("深拷贝......")
    print("a:", a)
    print("b:", b)


testCopy()
testDeepCopy()

