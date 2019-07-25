#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 8:29 AM
# @Author  : noduez
# @File    : uniCGI.py
# @Software: PyCharm

CODEC = 'UTF-8'
UNICODE_HELLO = u'''
Hello!
\u00A1Hola!
\u4F60\u597D!
\u3053\u3093\u306B\u3061\u306F!
'''
print('Content-Type: text/html; charset=%s\r' % CODEC)
print('\r')
print('<HTML><HEAD><TITLE>Unicode CGI Demo</TITLE><HEAD>')
print('<BODY>')
print(UNICODE_HELLO.encode(CODEC))
print('</BODY></HTML>')