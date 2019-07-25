from django.contrib import admin
from .models import *

class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'state', 'created_at')
# Register your models here.
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment)