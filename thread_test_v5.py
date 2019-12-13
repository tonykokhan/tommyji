# 多核CPU
#
# 如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。
# 如果写一个死循环的话，会出现什么情况呢？
# 打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。
# 我们可以监控到一个死循环线程会100%占用一个CPU。
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL
# 锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，
# 多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
#
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。所以，在
# Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单
# 易用的特点。不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL
# 锁，互不影响。

# 试试用Python写个死循环：

import threading
import multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()



