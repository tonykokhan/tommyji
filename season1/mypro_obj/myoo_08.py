# 方法的动态性
# Python是动态语言，我们可以动态的为类添加新的方法，或者动态的修改类的已有的方法。


# 测试方法的动态性
class Person:

    def work(self):
        print("努力上班！")


def play_game(s):
    print("{0}在玩游戏".format(s))


def work2(s):
    print("好好工作，努力上班！赚大钱，取媳妇！")


Person.play = play_game
p = Person()
p.work()
# p.play_game()   # AttributeError: 'Person' object has no attribute 'play_game'
p.play()    # Person.play(p)

Person.work = work2
p.work()
