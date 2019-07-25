__Author__ = "noduez"
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 10:57 AM
# @File    : mech.py 可以编程的 Web 浏览方式
# @Software: PyCharm

from bs4 import BeautifulSoup, SoupStrainer
from mechanicalsoup import Browser

br = Browser()

#home page
rsp = br.submit('http://us.pycon.org/2011/home')
print('\n***', rsp.geturl())
print("Confirm home page has 'Log in' link; click it")
page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
rsp = br.follow_link(text_regex='Log in')