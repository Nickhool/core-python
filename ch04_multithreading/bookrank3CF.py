__Author__ = "noduez"
'''高级任务管理'''

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen, Request

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/75.0.3770.90 Safari/537.36'
    headers = {'User-Agent': user_agent}
    req = Request('{0}{1}'.format(AMZN, isbn), headers=headers)  # or str.format
    with urlopen(req) as page:
        return str(REGEX.findall(page.read().decode('utf-8'))[0])

def _main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(
                ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s' % (ISBNs[isbn], ranking))

if __name__ == '__main__':
    _main()