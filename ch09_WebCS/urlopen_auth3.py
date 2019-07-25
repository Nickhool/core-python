__Author__ = "noduez"
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 9:23 AM
# @File    : urlopen_auth.py
# @Software: PyCharm

from urllib import request, error, parse

LOGIN = 'wesley'
PASSWD = "you'llNeverGuess"
URL = 'https://www.baidu.com'
REALM = 'Secure Archive'


def handler_version(url):
    from urllib.parse import urlparse
    hdlr = request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urlparse(url)[1], LOGIN, PASSWD)
    opener = request.build_opener(hdlr)
    request.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodebytes
    req =  request.Request(url)
    b64str = encodebytes(bytes('%s:%s' % (LOGIN, PASSWD), encoding='utf-8'))[:-1]
    req.add_header("Authorization","Basic %s" % b64str)
    return req


for funcType in ('handler', 'request'):
    print('*** Using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    f = request.urlopen(url)
    print(f.readline())
    f.close()
