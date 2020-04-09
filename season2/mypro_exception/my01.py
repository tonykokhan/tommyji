# Traceback 追溯，追根溯源。
# most recent call last 最后一次调用。

# a = 1/0


def a():
    num = 1 / 0


def b():
    a()


def c():
    b()


c()
