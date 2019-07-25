import re
import os

f = os.popen('who', 'r')
# f = open('whodata.txt', 'r')
for eachline in f:
	print re.split(r'\s\s+|\t', eachline.rstrip())
f.close()