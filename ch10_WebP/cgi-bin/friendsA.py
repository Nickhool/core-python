#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 7:13 PM
# @File    : friendsA.py
# @Software: PyCharm

import cgi

reshtml = '''Content-type: text/html; charset=UTF-8\n\n
<html><head><title>
Friends CGI Demo (dynamic screen)
</title></head>
<body><h3>Friends list for:<I>%s</I></h3>
Your name is: <b>%s</b><p>
You have <b>%s</b> friends.
</body></html>'''

form  = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml % (who, who, howmany))
