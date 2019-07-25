__Author__ = "noduez"

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

# multipart alertnative: text and html
def make_map_msg():
    email = MIMEMultipart('alertnative')
    text = MIMEText('Hello world!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>', 'html')
    email.attach(html)
    return email

# multipart: image
def make_img_msg(fn):
    f = open(fn, 'r')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
                     'attachment; filename="%s"' % fn)
    return email

def sendMsg(fr, to, msg):
    s = SMTP('localhost')
    errs = s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    SENDER = 'noduezhang@gmail.com'
    RECIPS = '1282622481@qq.com'
    SOME_IMAGE_FILE = '/Users/mac/Pictures/j1RH9B-0.jpg'

    print('Sending multipart alertnative msg...')
    msg = make_map_msg()
    msg['From'] = SENDER
    msg['To'] = ','.join(RECIPS)
    msg['Subject'] = 'multipart alertnative test'
    sendMsg(SENDER, RECIPS, msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg(SOME_IMAGE_FILE)
    msg['From'] = SENDER
    msg['To'] = ','.join(RECIPS)
    msg['Subject'] = 'image file test'
    sendMsg(SENDER, RECIPS, msg.as_string())