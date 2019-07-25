#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 5:05 PM
# @Author  : noduez
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from poster import views

urlpatterns = [
    url('^$', views.post_tweet, name='post_tweet'),
    url('^thankyou', views.thankyou, name='thankyou'),
    url('test', views.test, name='test'),
    url('^edit/(?P<tweet_id>\d+)$', views.post_tweet,
            name='post_tweet')
]