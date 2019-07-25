__Author__ = "noduez"
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 10:19 AM
# @File    : parse_links.py 链接解释器
# @Software: PyCharm

from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup, SoupStrainer, element
from html5lib import parse, treebuilders

URLs = {
    'http://python.org',
}

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url, f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))

def fasterBS(url, f):
    'fasterBS() - use BeautifulSoup to parse only anchor tags'
    only_a_tags = SoupStrainer("a")
    re =  BeautifulSoup(f, parse_only=only_a_tags)
    # print('---re[0]---', re[0])
    # print('---re[1]---', re[1])
    # print('---len---', len(re))

    # print('x:--+--+--',x)
    ostr = [urljoin(url, x['href']) for x in re]
    output(ostr)
    # output(urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def htmlparser(url, f):
    'htmlparser() - use HTMLParser to parse anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attrs[0] == 'href':
                    self.data.append(attrs[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)

def html5libparse(url, f):
    'html5libparse() - use html5lib to parse anchor tags'
    output(urljoin(url, x.attrbutes['href'])
           for x in parse(f) if isinstance(x, treebuilders) and x.name == 'a')

def process(url, data):
    print('\n*** simple BS')
    simpleBS(url, data)
    data.seek(0)
    print('\n*** faster BS')
    fasterBS(url, data)
    data.seek(0)
    print('\n*** HTMLParser')
    htmlparser(url, data)
    data.seek(0)
    print('\n*** HTML5lib')
    html5libparse(url, data)
    data.seek(0)

def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read().decode('utf-8'))
        f.close()
        process(url, data)

if __name__ == '__main__':
    main()