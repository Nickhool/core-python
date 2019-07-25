from django.test import TestCase

# Create your tests here.
EMAIL_HOST = 'smtp.qq.com'   #邮箱的smtp服务器地址
EMAIL_PORT = 25			#端口
EMAIL_HOST_USER = '*@qq.com'      #使用者邮箱
EMAIL_HOST_PASSWORD = 'gjvqyplldimwgdhi'     #第三方授权码
EMAIL_USE_TLS = False                 # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。
EMAIL_FROM = '1282622481@qq.com'            #发送者邮箱，就是发送者

from django.core.mail import send_mail
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    email_title = 'this is title'
    email_body = 'this is content'
    send_status = send_mail(email_title, email_body, EMAIL_FROM, ['994894722@qq.com'])