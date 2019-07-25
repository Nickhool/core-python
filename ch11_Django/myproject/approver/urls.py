#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 5:16 PM
# @Author  : noduez
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from approver.views import *

urlpatterns = [
    url('^$', list_tweet, name='list_tweet'),
    url('^review/(?P<tweet_id>\d+)$', review_tweet, name='review_tweet'),
]