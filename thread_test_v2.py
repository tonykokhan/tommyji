import threading
from threading import current_thread


class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = Mythread()
# 启动子进程t1
t1.start()
# 等待t1结束
t1.join()

print(current_thread().getName(), 'end')
