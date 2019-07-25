#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 9:45 AM
# @Author  : noduez
# @File    : wsgi_app.py
# @Software: PyCharm

from wsgiref.simple_server import make_server, demo_app

def simple_wsgi_app(environ, start_response):
    staus = '200 OK'
    headers = [('Content-type', 'text/plain')]
    return ['Hello world!']
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

# httpd = make_server('', 8088, simple_wsgi_app)
httpd = make_server('', 8088, demo_app)
print('Started app serving on port 8088...')
httpd.serve_forever()