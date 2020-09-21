# -*- coding: utf-8 -*-


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print(self.parent)
        print('Parent')

    # def bar(self, message):
    #    print message, 'from Parent'
    #    #print message


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild, self)将返回当前类继承的父类,即FooParent
        super(FooChild, self).__init__()
        print('Child')

    # def bar(self, message):
    #    super(FooChild, self).bar(message)
    #    print 'Child bar fuction'
    #    print self.parent


class FooKid(FooParent):
    def __init__(self):
        super(FooKid, self).__init__()
        print('Kid')


if __name__ == '__main__':
    fooChild = FooChild()  # 类的实例化,继承父类FooParent,所以要打印父类的方法
    fooKid = FooKid()
    # fooChild.bar('HelloWorld')
