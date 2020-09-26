# 进程间的通信：：（直接复制粘贴运行对照输出。。）
# 这种方法可以实现任意进程间的通信，这里写的是主、子进程间的通信
import multiprocessing


def foo(aa):
    ss = aa.get()  # 管子的另一端放在子进程这里，子进程接收到了数据
    print('子进程已收到数据...')
    print(ss)  # 子进程打印出了数据内容...


if __name__ == '__main__':  # 要加这行...

    tx = multiprocessing.Queue()  # 创建进程通信的Queue，你可以理解为我拿了个管子来...
    tx.put('有内鬼，终止交易！')  # 将管子的一端放在主进程这里，主进程往管子里丢入数据↑
    print('主进程准备发送数据...')
    jc = multiprocessing.Process(target=foo, args=(tx,))  # 创建子进程
    jc.start()  # 启动子进程
    jc.join()
