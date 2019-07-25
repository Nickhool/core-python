__Author__ = "noduez"
'''子类化的 Thread'''
'''派生 Thread 的子类，并创建子类的实例'''

import threading
from time import sleep, ctime
# from multithreading.myThread import MyThread

loops = [4,2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('Starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:        # start threads
        threads[i].start()

    for i in nloops:        # wait for all
        threads[i].join()   # threads to finish

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()