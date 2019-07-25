#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 3:28 PM
# @Author  : noduez
# @File    : friendsB.py
# @Software: PyCharm

import cgi

header = 'Content-type: text/html\n\n'

formhtml = '''<html><head><title>
Friends CGI Demo </title></head>
<body><h3>Friends list for: <i>NEW USER</i></h3>
    <form action="/cgi-bin/friendsB.py">
        <b>Enter your name:</b>
        <input type=hidden name=action value=edit>
        <input type="text" name="person" value="NEW USER" size=15>
        <p><b>How many friends do you have?</b></p>
        %s
        <p><input type="submit"></p>
    </form>
</body></html>'''

fradio = '<input type=radio name=howmany value="%s" %s> %s\n'

def showform():
    friends = []
    for i in (0,10,25,50,100):
        checked = ''
        if i == 0:
            checked = 'CHECKED'
        friends.append(fradio % (str(i), checked, str(i)))

    print('%s%s' % (header, formhtml %  ''.join(friends)))

reshtml = '''<html><head><title>
Friends CGI Demo
</title></head>
<body><h3>Friends list for:<I>%s</I></h3>
Your name is: <b>%s</b><p>
You have <b>%s</b> friends.
</body></html>'''

def doResults(who, howmany):
    print(header + reshtml % (who, who, howmany))

def process():
    form = cgi.FieldStorage()
    if 'person' in form:
        who = form.getvalue('person')
    else:
        who = 'NEW USER'
    if 'howmany' in form:
        howmany = form.getvalue('howmany')
    else:
        howmany = 0
    if 'action' in form:
        doResults(who, howmany)
    else:
        showform()

if __name__ == '__main__':
    process()