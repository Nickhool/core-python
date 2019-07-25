#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 5:19 PM
# @Author  : noduez
# @File    : friendsC.py
# @Software: PyCharm

import cgi
from urllib.request import quote

header = 'Content-type: text/html\n\n'
url = '/cgi-bin/friendsC.py'

errorhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s<B><P>
<FORM><INPUT TYPE=button VALUE=Back 
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

def showError(error_str):
    print(header + errorhtml % error_str)

formhtml = '''<html><head><title>
Friends CGI Demo </title></head>
<body><h3>Friends list for: <i>%s</i></h3>
    <form action="%s">
        <b>Enter your name:</b>
        <input type=hidden name=action value=edit>
        <input type="text" name="person" value="%s" size=15>
        <p><b>How many friends do you have?</b></p>
        %s
        <p><input type="submit"></p>
    </form>
</body></html>'''

fradio = '<input type=radio name=howmany value="%s" %s> %s\n'

def showform(who, howmany):
    friends = []
    for i in (0,10,25,50,100):
        checked = ''
        if str(i) == howmany:
            checked = 'CHECKED'
        friends.append(fradio % (str(i), checked, str(i)))

    print('%s%s' % (header, formhtml % (who, url, who, ''.join(friends))))

reshtml = '''<html><head><title>
Friends CGI Demo
</title></head>
<body><h3>Friends list for:<I>%s</I></h3>
Your name is: <b>%s</b><p>
You have <b>%s</b> friends.
<P>Click <a href="%s">here</a> to edit your data again</P>
</body></html>'''

def doResults(who, howmany):
    newurl = url + '?action=reedit&person=%s&howmany=%s' % (quote(who), howmany)
    print(header + reshtml % (who, who, howmany, newurl))

def process():
    error = ''

    form = cgi.FieldStorage()
    if 'person' in form:
        who = form.getvalue('person').title()
    else:
        who = 'NEW USER'
    if 'howmany' in form:
        howmany = form.getvalue('howmany')
    else:
        if 'action' in form and form.getvalue('action') == 'edit':
            error = 'Please select number of friends!'
        else:
            howmany = 0
    if not error:
        if 'action' in form and form.getvalue('action') != 'reedit':
            doResults(who, howmany)
        else:
            showform(who, howmany)
    else:
        showError(error)

if __name__ == '__main__':
    process()