#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 5:55 PM
# @Author  : noduez
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import *
from blog import views

urlpatterns = [
    # 主页
    url(r'^$', views.archive, name='archive'),

    url(r'^create/', views.create_blogpost, name='create_blogpost'),
]