from __future__ import with_statement
__Author__ = "noduez"
'''锁示例'''

from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)

loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()
lock = Lock()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    # print('[%s] Started %s' % (ctime(), myname))
    print('[{0}] Started {1}'.format(ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    # print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('[{0}] Completed {1} ({2} secs)'.format(ctime(), myname, nsec))
    # print('   (remaining: %s)' % (remaining or 'NONE'))
    print('   (remaining: {0})'.format(remaining or 'NONE'))
    lock.release()

# 使用上下文管理 简化代码 省略 acquire 和 release（实际使用with后自动执行）
def loop1(nsec):
    myname = currentThread().name
    with lock:
        remaining.add(myname)
        print('[{0}] Started {1}'.format(ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[{0}] Completed {1} ({2} secs)'.format(ctime(), myname, nsec))
        print('   (remaining: {0})'.format(remaining or 'NONE'))

def _main():
    for pause in loops:
        Thread(target=loop1, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()