__Author__ = "noduez"
import re

#%%
# 1-1 匹配字符串
pattern = r'[bh][aiu]t'
string = 'asdfbatkkjbitllwbutpphatoouhitwwhut'
print(re.findall(pattern, string))

# patt = '[bh][aiu]t'
# list = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
# for v in list:
#     if re.match(patt, v):
#         print('---'+v)

# 1-2 姓 + 名
patt = '[A-Za-z]+ [A-Za-z]+'

# 1-3 单个逗号和单个空白分隔符
patt = '[A-Za-z]+, [A-Za-z]+'

# 1-4 Python标识符
patt = '[A-Za-z]\w*'

# 1-5 匹配街道地址
# patt = r'\d+(\s[A-Za-z]+)*'
pattern = r'\d+ [A-Za-z ]+'
string1 = '1180 Bordeaux Drive'
string2 = '3120 De la Cruz Boulevard'
print(re.match(pattern, string1).group())
print(re.match(pattern, string2).group())

# 1-6 匹配简单Web域名
patt = '((http:|https:)//)?[w]{3}\.\w+(.edu|.com|.net)'
string = 'http://www.fool.edu'
print(re.match(patt, string).group())

# 1-7 Python整数
patt = '-?(\d+)'
string = '-2342342'
print(re.match(patt, string).group())

# 1-7 Python长整数
patt = '-?(\d+)L'
string = '-2342342L'
print(re.match(patt, string).group())

# 1-9 Python浮点数
pattern = r'-?\d+\.\d+'
string = '3.1415926'
print(re.match(pattern, string).group())

# 1-10 Python复数
pattern = r'-?\d+\.?\d+\+\d+\.+\d+j'
string = '-1.4+1.5j'
print(re.match(pattern, string).group())

# 1-11 电子邮件
pattern = r'\w+@\w+\.com'
string = 'abc_abc111@abc111_abc.com'
print(re.match(pattern, string).group())

# 1-12 匹配所有能够表示有效的网址的集合（URL）
pattern = r'((http:|https:)//)?([w]{3}\.)?\w+\.\w+'
string = 'http://foothill.edu'
print(re.match(pattern, string).group())

# 1-14 剩余3个月
pattern = r'1[0-2]'
string = '12'
print(re.search(pattern, string).group())

# 1-15 处理信用卡号码
pattern = r'([0-9]{4}-[0-9]{6}-[0-9]{5})|([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})'
string = '4444-444465-44446'
print(re.search(pattern, string).group())

# 1-17
week_list = []
month_list = []
f = open('redata.txt', 'r')
for eachLine in f:
    week_list.append(re.split(r'\s+', eachLine)[0])
    month_list.append(re.split(r'\s+', eachLine)[1])

week_day_tmp_list = set(week_list)
month_tmp_list = set(month_list)
print("____________________")
print("Week Times:")
for item in week_day_tmp_list:
    print("%s appears %d time(s)" %(item, week_list.count(item)))

print("____________________")
print("Month Times:")
for item in month_tmp_list:
    print("%s appears %d time(s)" %(item, month_list.count(item)))
f.close()

# 1-18 通过确认整数字段中的第一个整数匹配在
# 每个输出行起始部分的时间戳，确保在redata.txt中没有数据损坏
from time import ctime

num_pattern = r'.+::(\d+)-'
time_stamp_pattern = r'^(.{24})::.+'
try:
    f = open('redata.txt', 'r')
    for i, eachLine in enumerate(f):
        # 得到第一个整数
        second = re.search(num_pattern, eachLine.strip()).group(1)
        time_stamp_str = re.search(time_stamp_pattern, eachLine.strip()).group(1)
        # 匹配时间戳是否正确
        if time_stamp_str != str(ctime(int(second))):
            print("Line %d is not WRONG! Correct Timestamp is %s" %(i, time_stamp_str))
        else:
            print("This Line is OK!")
except ValueError as value_err:
    print("First Num Is Not The Type Of INT:" + value_err.message)
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-19 提取每行中完整的时间戳
time_stamp_pattern = r'^(.{24})::.+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.search(time_stamp_pattern, eachLine.strip()).group(1))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-20 提取每行中完整的电子邮件地址
email_pattern = r'.+::(.+)::.+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.search(email_pattern, eachLine.strip()).group(1))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-21 仅仅提取时间戳中的年份
month_pattern = r'^\w{3}\s(\w{3}).+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.search(month_pattern, eachLine.strip()).group(1))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-22 仅仅提取时间戳中的年份
year_pattern = r'.+(\d{4})::.+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.search(year_pattern, eachLine.strip()).group(1))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-23
time_pattern = r'.+(\d{2}:\d{2}:\d{2}).+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.search(time_pattern, eachLine.strip()).group(1))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-24 仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名一起提取）
pattern = r'.+::(\w+)@(\w+\.\w+).+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        # 登录名
        print(re.search(pattern, eachLine.strip()).group(1))
        # 主域名和高级域名
        print(re.search(pattern, eachLine.strip()).group(2))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-25 仅仅从电子邮件地址中提取登录名和域名（包括主域名和高级域名）
pattern = r'.+::(\w+)@(\w+)\.(\w+).+'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        # 登录名
        print(re.search(pattern, eachLine.strip()).group(1))
        # 主域名
        print(re.search(pattern, eachLine.strip()).group(2))
        # 高级域名
        print(re.search(pattern, eachLine.strip()).group(3))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

#1-26 使用你的电子邮件地址替换每一行数据中的电子邮件地址。
pattern = r'(.+::)(\w+@\w+\.\w+)(::.+)'
my_email = r'\1snowfall_dan@outlook.com\3'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.sub(pattern, my_email, eachLine.strip()))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-27
pattern = r'(.+)(\w{3})\s(\d{2})(.+)(\d{4})(.+)'
my_email = r'\1\3 \2\4\5\6'
try:
    f = open('redata.txt', 'r')
    for eachLine in f:
        print(re.sub(pattern, my_email, eachLine.strip()))
except IOError as io_err:
    print('File Error:' + io_err.message)
finally:
    f.close()

# 1-28  区号（三个整数集合中的第一部分和后面的连字符）是可选的
pattern = r'(\d{3}-)?\d{3}-\d{4}'
phone = '555-1212'
print(re.match(pattern, phone).group())

# 1-29
pattern = r'(\d{3}-|\(\d{3}\)-|\d{3}-)?\d{3}-\d{4}'
phone1 = '(888)-555-1212'
phone2 = '555-1212'
phone3 = '888-555-1212'
print(re.match(pattern, phone1).group())
print(re.match(pattern, phone2).group())
print(re.match(pattern, phone3).group())
