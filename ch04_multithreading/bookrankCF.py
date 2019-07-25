__Author__ = "noduez"
'''concurrent.futures 模块'''

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)' \
                 ' AppleWebKit/537.36 (KHTML, like Gecko)' \
                 ' Chrome/75.0.3770.90 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = Request('%s%s' % (AMZN, isbn), headers=headers) # or str.format
    page = urlopen(req)
    data = page.read().decode('utf-8')
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('- %r ranked %s' %
          (ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn in ISBNs:
            executor.submit(_showRanking, isbn)
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()