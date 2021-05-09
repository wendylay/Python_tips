"""python简洁使用正则对列表元素进行筛选, 并生成新列表
refer link: https://blog.csdn.net/liaowhgg/article/details/86667938"""

import os
import re

print(list(filter(lambda x: x % 2, range(10)))) 
file_list = os.listdir(path='F:/')

filter_list = list(filter(lambda x: re.match(r'.*txt',x), file_list))[0]