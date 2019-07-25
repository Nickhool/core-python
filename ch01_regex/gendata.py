__Author__ = "noduez"

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
f=open('redata.txt','w')
for i in range(randrange(5, 11)):
    dtint = randrange(922337205)      # pick date
    dtstr = ctime(dtint)            # date string
    llen = randrange(4, 8)          # login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)      #domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    # print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
    #     dom, choice(tlds), dtint, llen, dlen))
    input = str(dtstr) + '::' + str(login) + '@' + str(dom) + '.' + str(choice(tlds)) + '::' + str(dtint) + '-' + str(
        llen) + '-' + str(dlen)
    f.write(input + '\n')