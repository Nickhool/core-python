from django.contrib import admin
from ch11_Django.mysite.blog import models

# Register your models here.

admin.site.register(models.BlogPost)
""" error: ModuleNotFoundError: No module named 'ch11_Django'"""
""" error: ModuleNotFoundError: No module named 'mysite.blog' """
'''就此打住 另起目录 作为单独项目运行'''


