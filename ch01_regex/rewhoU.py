__Author__ = "noduez"

import os
from distutils.log import warn as printf
import re

with os.popen('who', 'r') as f:
    for eachline in f:
        printf(re.split(r'\s\s+|\t', eachline.strip()))