__Author__ = "noduez"
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 11:29 AM
# @File    : setup.py
# @Software: PyCharm
from distutils.core import setup, Extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[
    Extension(MOD, sources=['Extest2.c'])])